"""
一、数据类型分类

Python 里的数据类型分类为：
1、数值类型
    * bool：布尔类型，唯二的值是 True、False
    * int：整数类型，如 10、-20、0
    * float：浮点数类型，如 3.14、10.0

2、字符串类型
    * str：字符串类型，如 "Hello Python"

3、容器类型
    * list：列表，如 [ 1, 2, 3 ]
    * dict：字典，如 { "name": "张三", "age": 18 }
    * set：集合，如 { 1, 2, 3 }
    * tuple：元组，如 ( 1, 2, 3 )

4、空类型
    * NoneType：空类型，唯一的值是 None
      None 类似于 Java 里的 null，但不完全一样。Java 里的 null 是引用类型变量的附属值，而 Python 里的 None 则是一个真实存在的独立对象，用来表示“空值”或“没有值”

需要注意的是：Python 里所有的数据类型都是引用类型，所有的值都是对象
其中 bool、int、float、str、tuple 是不可变对象，list、dict、set 是可变对象
"""
test_str = "Hello Python"
print(test_str)  # Hello Python

"""
二、type() 和 isinstance()

* type(obj)：用来获取某个对象所属的数据类型，也可以用来精准判断某个对象是不是某个数据类型的实例
* isinstance(obj, 数据类型)：用来判断某个对象是不是某个数据类型或其子类的实例
"""
print(type(test_str))  # <class 'str'>
print(type(test_str) is str)  # True
print(isinstance(test_str, str))  # True

"""
三、数据类型强转

Python 里一般使用数据类型名作为转换函数来完成数据类型强转：目标类型(变量)

i = 10
d = float(i)
print(d)  # 10.0
"""
# 转 bool（什么都能转）
# 0、0.0、空字符串、空列表、空字典、空集合、空元组、None 转成 bool 都是 False
# 其它值转成 bool 都是 True
print(bool(1))  # True
print(bool(0))  # False

print(bool(3.14))  # True
print(bool(0.0))  # False

print(bool("Hello"))  # True
print(bool(""))  # False

print(bool([1, 2, 3]))  # True
print(bool([]))  # False

print(bool({"name": "张三"}))  # True
print(bool({}))  # False

print(bool({1, 2, 3}))  # True
print(bool(set()))  # False

print(bool((1, 2, 3)))  # True
print(bool(()))  # False

print(bool(None))  # False

# 转 int（容器类型、空类型不能转）
print(int(True))  # 1
print(int(False))  # 0

print(int(3.14))  # 3，float 转 int 时，不是四舍五入，而是直接去掉小数部分
print(int(-3.14))  # -3

print(int("123"))  # 123
print(int("-20"))  # -20
# int("3.14")       # 报错，如果字符串是小数，得先转成 float，再转成 int
# int("abc")        # 报错
# int("")           # 报错

# 转 float（容器类型、空类型不能转）
print(float(True))  # 1.0
print(float(False))  # 0.0

print(float(10))  # 10.0
print(float(-20))  # -20.0

print(float("3.14"))  # 3.14
print(float("10"))  # 10.0
print(float("-20.5"))  # -20.5
# int("abc")          # 报错
# int("")             # 报错

# 转 str（什么都能转）
print(str(True))  # "True"
print(str(False))  # "False"

print(str(10))  # "10"
print(str(-20))  # "-20"

print(str(3.14))  # "3.14"

print(str([1, 2, 3]))  # "[1, 2, 3]"
print(str({"name": "张三", "age": 18}))  # "{'name': '张三', 'age': 18}"
print(str({1, 2, 3}))  # "{1, 2, 3}"
print(str((1, 2, 3)))  # "(1, 2, 3)"

print(str(None))  # "None"

# 转 list（数值类型、空类型不能转）
print(list("abc"))  # ['a', 'b', 'c']

print(list((1, 2, 3)))  # [1, 2, 3]
print(list({1, 2, 3}))  # [1, 2, 3]
print(list({"name": "张三", "age": 18}))  # dict 转 list，默认取 key 来组成数组 ['name', 'age']
print(list({"name": "张三", "age": 18}.values()))  # dict 转 list，也可以取 value 来组成数组 ['张三', 18]
print(list({"name": "张三", "age": 18}.items()))  # dict 转 list，还可以取 key-value 构成的元组来组成数组 [('name', '张三'), ('age', 18)]
