"""
【LLM 实现金融文本分类】需求：我们提供几个固定的类型，然后随便输入一段金融领域文本，大模型能够判断这段文本属于什么类型
"""

"""
导入 ollama 后，ollama 会立刻初始化 Client()；但是我们电脑的环境里有 ALL_PROXY=socks5://127.0.0.1:49979，于是 httpx 走 SOCKS 代理逻辑，但当前环境没有 socksio，所以抛了异常：
ImportError: Using SOCKS proxy, but the 'socksio' package is not installed

我们可以通过如下代码，让这个脚本不继承代理，import ollama 之前加：

import os

for k in [
  "ALL_PROXY", "all_proxy",
  "HTTP_PROXY", "http_proxy",
  "HTTPS_PROXY", "https_proxy",
  "NO_PROXY", "no_proxy",
]:
  os.environ.pop(k, None)
"""
import os

for k in [
    "ALL_PROXY", "all_proxy",
    "HTTP_PROXY", "http_proxy",
    "HTTPS_PROXY", "https_proxy",
    "NO_PROXY", "no_proxy",
]:
    os.environ.pop(k, None)

# 导入 ollama 框架
# 因为我们要使用 ollama 本地部署的大模型
# ollama 的 api 在接收用户输入时，要求输入一个类似下面这样的 messages 数组，包含系统系统词、所有的对话历史
# 所以我们得把系统提示词、所有的对话历史手动构建成这样的结构
# {
#   "messages": [
#     // 这里是系统提示词的角色部分
#     {
#       "role": "system",
#       "content": "你是一个地理老师"
#     },
#     // 注意：这里是系统提示词的示例部分（严格来讲叫“少样本示例”），而不是用户提示词，用来让模型参考学习的
#     {
#       "role": "user",
#       "content": "中国的首都是哪里？"
#     },
#     {
#       "role": "assistant",
#       "content": "北京"
#     },
#
#     // 这里是之前的对话历史
#     {
#       "role": "user",
#       "content": "浙江的省会是哪里？"
#     },
#     {
#       "role": "assistant",
#       "content": "杭州"
#     },
#
#     // 这里是本轮对话的用户问题
#     {
#       "role": "user",
#       "content": "西湖在哪个区？"
#     }
#   ]
# }
import ollama

client = ollama.Client("http://localhost:11434")

# 元数据
# 从元数据中我们可以得到“我们提供几个固定的类型”
# 从元数据中我们可以构造出系统提示词里的示例部分
__meta_data = {
    "新闻报道": "某新能源企业发布上半年产销数据，整车销量同比增长 28%，海外订单持续扩容，机构看好其海外市场渗透率进一步提升。",
    "财务报告": "公司 2025 年归母净利润 12.6 亿元，同比增长 15.3%；营收 89 亿元，毛利率小幅上行，经营性现金流净额持续维持正向水平。",
    "公司公告": "公司公告筹划非公开发行股票事项，拟募集资金投向新建生产基地，本次事项尚需股东大会及证监会审批，存在不确定性。",
    "分析师报告": "受益行业景气上行，上调公司盈利预测，预计 2026-2027 业绩持续兑现，给予 “增持” 评级，目标价对应 22 倍合理估值。"
}


def __get_all_type_list():
    # 从元数据中得到“我们提供几个固定的类型”
    all_type_list = list(__meta_data.keys())

    return all_type_list


def __build_system_prompt():
    all_type_list = __get_all_type_list()

    # 系统提示词 = 角色 + 背景 + 目标 + 约束 + 示例
    # 角色：你是一个金融文本分类专家。
    # 背景：我们会给你提供几个固定的类型：{all_type_list}。
    # 目标：我们还会给你提供一段文本，你需要理解这段文本的含义，并精准判定这段文本是哪种类型。如果你觉得不属于任何类型，那就输出：未知类型
    # 约束：一段文本只可能对应一个类型
    system_prompt = [
        {
            "role": "system",
            "content": f"你是一个金融文本分类专家。"
                       f"我们会给你提供几个固定的类型：{all_type_list}。"
                       f"我们还会给你提供一段文本，你需要理解这段文本的含义，并精准判定这段文本是哪种类型。"
                       f"一段文本只可能对应一个类型。最终输出只输出类型，不要解释。"
        }
    ]
    # 示例
    for key, value in __meta_data.items():
        system_prompt.append({
            "role": "user",
            "content": f"'{value}' 是 {all_type_list} 中的什么类型？"
        })
        system_prompt.append({
            "role": "assistant",
            "content": f"{key}"
        })

    return system_prompt


def __inference(user_input):
    all_type_list = __get_all_type_list()
    system_prompt = __build_system_prompt()

    # 根据用户输入构建用户提示词
    user_prompt = {
        "role": "user",
        "content": f"'{user_input}' 是 {all_type_list} 中的什么类型？"
    }
    print(f"本轮用户提示词 = {user_prompt}")

    # 构建最终发给 ollama 的 messages 数组
    # Python 中的 * 类似于其它语言里的 ...，用来将数组、Map 等打散成元素
    messages = [
        *system_prompt,
        user_prompt
    ]

    response = client.chat("deepseek-r1:7b", messages)
    print(f"本轮模型回复 = {response.message.content}")


if __name__ == "__main__":
    user_input_list = [
        "央行宣布下调 MLF 利率 10 个基点，市场预判后续 LPR 同步下调，有望降低实体企业融资成本，提振地产消费需求。",
        "本期资产负债率小幅上升至 62%，主要系扩产新增长期借款；存货规模增加，管理层提示需关注下游需求波动带来减值风险。",
        "公司披露高管减持计划进展，副总经理已通过集中竞价减持 0.32% 股份，减持完成后不再持有公司无限售流通股份。",
        "行业竞争加剧压制产品价格，下调全年盈利预期，短期盈利承压，维持 “中性” 评级，重点跟踪公司新品落地进度。",
        "今天天气很好"
    ]

    for user_input in user_input_list:
        __inference(user_input)
