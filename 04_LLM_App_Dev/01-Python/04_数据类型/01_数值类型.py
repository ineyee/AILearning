from decimal import Decimal

"""
一、布尔类型 bool
Python 里的布尔类型只有 True、False 两个取值
"""
v1 = True
print(v1)  # True

v2 = False
print(v2)  # False

"""
二、整型 int
Python 里的整型理论上可以表示任意大小的整数，它的大小主要受内存限制、没有固定占多少位
"""
v1 = 10
print(v1)  # 10

big_num = 999999999999999999999
print(big_num)  # 999999999999999999999

"""
三、浮点数类型 float
Python 里的浮点数类型通常对应 C 语言里的 double，即双精度浮点数，也存在小数精度问题
"""
v1 = 3.1415926897123456789
print(v1)  # 3.1415926897123456

"""
四、高精度计算 Decimal
1、首先要知道，float 是有精度问题的
比如：0.7 * 0.7
数学上应该等于：0.49

但是在 Python 里，float 使用二进制浮点数存储
像 0.7 这种十进制小数，无法被二进制精确表示，所以实际存储的是一个近似值
因此参与计算时，结果可能不是精确的 0.49，而是 0.48999999999999994

小数计算丢精度的问题，本质上不是运算本身导致的
而是很多十进制小数在二进制浮点数中存储时就已经是近似值了

2、Decimal 怎么使用？
Python 里使用 decimal 模块里的 Decimal 可以解决此问题
建议使用字符串初始化 Decimal：Decimal("0.7")
不建议使用 float 初始化 Decimal：Decimal(0.7)，因为 Decimal(0.7) 接收到的已经不是数学意义上的精确 0.7，而是 float 近似值
"""
# 金钱计算丢精度的问题
d1 = 0.7
d2 = 0.7
d3 = d1 * d2
print(d3)  # 0.48999999999999994

# 不建议使用 float 初始化 Decimal
bd = Decimal(0.7)
print(bd)  # 0.6999999999999999555910790149937383830547332763671875

# 建议使用字符串初始化 Decimal
bd1 = Decimal("0.7")
bd2 = Decimal("0.7")
print(bd1 + bd2)  # 1.4
print(bd1 - bd2)  # 0.0
print(bd1 * bd2)  # 0.49
print(bd1 / bd2)  # 1
