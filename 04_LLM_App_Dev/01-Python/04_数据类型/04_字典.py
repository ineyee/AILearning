"""
Python 里的字典是可变字典：
* 无序
* key 不可以重复
* value 可以是任意类型
"""

"""
1、字典的声明及初始化
"""
dict1 = {}
dict11 = {
    "name": "张三",
    "age": 18,
    "height": 1.88
}
print(dict1)  # {}
print(dict11)  # {'name': '张三', 'age': 18, 'height': 1.88}

"""
2、字典的基本操作
"""
dict2 = {}

# 增
dict2["name"] = "张三"
dict2["age"] = 18
dict2["height"] = 1.88
print(dict2)  # {'name': '张三', 'age': 18, 'height': 1.88}

# 删
del dict2["height"]
print(dict2)  # {'name': '张三', 'age': 18}

# 改
dict2["age"] = 19
print(dict2)  # {'name': '张三', 'age': 19}

# 查
age = dict2["age"]
print(age)  # 19

"""
3、字典的遍历
"""
dict3 = {
    "name": "张三",
    "age": 18,
    "height": 1.88
}

# （1）只遍历 key
for key in dict3:
    print(key)
for key in dict3.keys():
    print(key)

# （2）只遍历 value
for value in dict3.values():
    print(value)

# （3）同时遍历 key、value
for key, value in dict3.items():
    print(key, value)

"""
4、字典的其它操作
"""
dict4 = {
    "name": "张三",
    "age": 18,
    "height": 1.88
}

# 获取字典的长度
print(len(dict4))  # 3

# 判断字典是否为空
print(len(dict4) == 0)  # False
print(not dict4)  # False

# 判断字典里是否包含某个 key
print("name" in dict4)  # True
print("name" in dict4.keys())  # True

# 判断字典里是否包含某个 value
print("张三" in dict4.values())  # True
