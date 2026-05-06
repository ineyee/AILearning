# 导入 httpx，用来请求天气接口
import httpx
# 导入 FastMCP，用来创建 MCP Server
from mcp.server.fastmcp import FastMCP


# ── 创建 MCP Server ───────────────────────────────────────────────────────────
# "weather-mcp-server" 是 MCP Server 的名字，编排器会用这个名字识别该服务
mcpServer = FastMCP("weather-mcp-server")


# ── 常量 ──────────────────────────────────────────────────────────────────────
# Open-Meteo 是一个开源、免费、无需鉴权的天气 API
OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

# WMO 标准的天气代码 --> 中文描述的映射表
# Open-Meteo API 返回的天气状况是一个符合 WMO 标准的数字代码而不是文字，比如 1
# 如果没有这个映射表的话，当前 MCP Server 里的工具返回给编排器的结果就是“天气：1”，编排器会把“天气：1”传递给模型，虽然模型最终也能理解“天气：1”的含义，但是不如“天气：基本晴朗”来得清晰直接
# 所以我们把这个映射关系在 MCP Server 内部做掉，让工具返回的结果对人和模型都开箱即读
WMO_CODE_MAP = {
    0:  "晴天",
    1:  "基本晴朗",
    2:  "局部多云",
    3:  "阴天",
    45: "雾",
    48: "冻雾",
    51: "小毛毛雨",
    53: "中毛毛雨",
    55: "大毛毛雨",
    61: "小雨",
    63: "中雨",
    65: "大雨",
    71: "小雪",
    73: "中雪",
    75: "大雪",
    77: "冰粒",
    80: "小阵雨",
    81: "中阵雨",
    82: "强阵雨",
    85: "小阵雪",
    86: "大阵雪",
    95: "雷暴",
    96: "雷暴伴小冰雹",
    99: "雷暴伴大冰雹",
}


# ── 私有函数 ───────────────────────────────────────────────────────────────────
def _wmo_to_desc(code: int) -> str:
    """
    将 WMO 标准的天气代码转换为中文描述

    参数:
        code: 天气代码

    返回:
        中文描述，未知天气代码则返回原始数字
    """
    return WMO_CODE_MAP.get(code, f"未知天气（代码 {code}）")


# ── MCP Server 的工具 1：根据经纬度查询当天的天气───────────────────────────────────
# @mcpServer.tool() 是一个装饰器，@ 后面跟着的就是我们上面创建的 MCP Server 实例，.tool() 固定写法，它的作用就是把当前函数注册到 mcpServer 实例上
# 一旦注册，当前函数就不再是一个普通的 Python 函数，而是一个可供编排器调用的工具
# 并且 mcpServer 实例还会把当前函数的函数名、参数&参数类型、docstring（也就是 """xxx""" 部分）生成工具的使用说明（即元数据）暴露给外界，这样一来模型就知道什么时候该调用当前工具、该给当前工具传递什么参数
@mcpServer.tool()
def get_current_weather(latitude: float, longitude: float) -> str:
    """
    根据经纬度查询当天的天气

    参数:
        latitude: 纬度，范围 -90 ~ 90（正数为北纬）
        longitude: 经度，范围 -180 ~ 180（正数为东经）

    返回:
        格式化后的天气文本，包含气温、风速、风向、天气状况、白天/夜晚
    """
    # API 需要接收的参数
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "timezone": "auto",
    }

    # 发起 HTTP 请求并获取响应
    response = httpx.get(OPEN_METEO_BASE_URL, params=params, timeout=30)
    # 非 2xx 状态码时抛出异常
    response.raise_for_status()

    # response 转换成 json
    data = response.json()
    # 获取 json 里的 current_weather 字段
    cw = data["current_weather"]

    # 解析各字段
    temp        = cw["temperature"]       # 气温（°C）
    windspeed   = cw["windspeed"]         # 风速（km/h）
    winddeg     = cw["winddirection"]     # 风向（度，0=北，90=东）
    weathercode = cw["weathercode"]       # WMO 天气代码
    is_day      = cw["is_day"]            # 1=白天，0=夜晚

    day_night = "白天" if is_day else "夜晚"
    weather_desc = _wmo_to_desc(weathercode)

    # 工具的执行结果
    return (
        f"📍 坐标：{data['latitude']}°N, {data['longitude']}°E\n"
        f"🕐 观测时间：{cw["time"]}（{data["timezone"]}）\n"
        f"🌡 气温：{temp}°C\n"
        f"💨 风速：{windspeed} km/h，风向：{winddeg}°\n"
        f"🌤 天气：{weather_desc}\n"
        f"☀️ 昼夜：{day_night}"
    )

# ── MCP Server 的工具 2：根据经纬度查询未来 7 天的天气──────────────────────────────
@mcpServer.tool()
def get_daily_forecast(latitude: float, longitude: float) -> str:
    """
    根据经纬度查询未来 7 天的天气

    参数:
        latitude: 纬度，范围 -90 ~ 90（正数为北纬）
        longitude: 经度，范围 -180 ~ 180（正数为东经）

    返回：
        格式化后的每天的日期、最高/最低气温、天气状况
    """
    # API 需要接收的参数
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,weathercode",
        "forecast_days": 7,
        "timezone": "auto",
    }

    # 发起 HTTP 请求并获取响应
    response = httpx.get(OPEN_METEO_BASE_URL, params=params, timeout=30)
    # 非 2xx 状态码时抛出异常
    response.raise_for_status()

    # response 转换成 json
    data  = response.json()
    # 获取 json 里的 daily 字段，包含各数组
    daily = data["daily"]

    # 解析各字段
    dates    = daily["time"]                  # 日期列表
    temp_max = daily["temperature_2m_max"]    # 每日最高气温
    temp_min = daily["temperature_2m_min"]    # 每日最低气温
    codes    = daily["weathercode"]           # 每日天气代码

    lines = [f"📅 未来 7 天天气预报（{data['timezone']}）\n"]
    for date, tmax, tmin, code in zip(dates, temp_max, temp_min, codes):
        desc = _wmo_to_desc(code)
        lines.append(f"  {date}  {tmin}°C ~ {tmax}°C  {desc}")

    # 工具的执行结果
    return "\n".join(lines)


# ── 入口 ──────────────────────────────────────────────────────────────────────
# Python 惯例：只有直接运行该脚本时才执行后续代码，被其它模块 import 时不会执行后续代码
# 对于 MCP Server 来说，就是防止别人 import 这个文件时意外启动服务器
if __name__ == "__main__":
    # 启动 MCP Server
    # transport="stdio" 表示 MCP Server 通过标准输入/输出与编排器通信，一般都是这种通信方式，默认就是这种通信方式
    mcpServer.run(transport="stdio")