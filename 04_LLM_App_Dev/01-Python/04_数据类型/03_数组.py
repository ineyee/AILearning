"""
Python 里的数组是可变数组：
* 有序
* 元素可重复
* 可以存储不同类型的元素，但实际开发中建议存放相同类型的元素
"""

"""
1、数组的声明及初始化
"""
list1 = []
list11 = [1, 2, 3]
print(list1)  # []
print(list11)  # [1, 2, 3]

"""
2、获取列表的长度
"""
list2 = [1, 2, 3]
print(len(list2))  # 3

"""
3、判断数组是不是空
"""
list3 = []
list33 = [1, 2, 3]
print(len(list3) == 0)  # True
print(len(list33) == 0)  # False
print(not list3)  # True
print(not list33)  # False

"""
4、数组增
"""
list4 = [1, 2, 3]

# （1）尾部增
list4.append(4)  # 单增
list4.extend([5, 6, 7])  # 批量增
print(list4)  # [1, 2, 3, 4, 5, 6, 7]

# （2）头部增、中间增
list4.insert(0, 0)  # 单增
list4[0:0] = [-3, -2, -1]  # 批量增，[0:0] 代表从 index = 0 开始
list4.insert(5, 15)  # 单增
list4[11:11] = [61, 62, 63]
print(list4)  # [-3, -2, -1, 0, 1, 15, 2, 3, 4, 5, 6, 61, 62, 63, 7]

"""
5、数组删
"""
list5 = [1, 2, 3]

# （1）删除某个下标处的元素
del list5[1]
print(list5)  # [1, 3]

# （2）删除某个元素
list5.remove(3)
print(list5)  # []

list5.extend([2, 3, 4])

# （3）批量删除元素
list5 = [item for item in list5 if item not in [2, 4]]
print(list5)  # [1, 3]

# （4）清空数组
list5.clear()
print(list5)  # []

"""
6、数组改
"""
list6 = [1, 2, 3]
list6[1] = 222
print(list6)  # [1, 222, 3]

"""
7、数组查
"""
list7 = [1, 2, 3]

# （1）查某个下标处的元素
print(list7[0])  # 1

# （2）查某个元素的下标
print(list7.index(1))  # 0

# （3）数组里是否包含元素
print(1 in list7)  # True

# （4）截取子数组（前闭后开）
print(list7[0:2])  # [1, 2]，从下标 0 开始截取到 2（不包含 2）
print(list7[1:])  # [2, 3]，从下标 1 开始截取到最后
print(list7[:1])  # [1]，从下标 0 开始截取到 1（不包含 1）
print(list7[:])  # [1, 2, 3]，复制整个数组

"""
8、数组的遍历
"""
list8 = [1, 2, 3]

# （1）for 遍历法
for item in list8:
    print(item)

# （2）遍历时删除元素
# 千万不要一边遍历数组，一边删除原数组里的元素，因为删除元素会改变数组的长度和下标，容易导致数据错乱
# 推荐把原数组复制出来一份，遍历这个副本，然后删除原数组里的相同元素
for item in list8[:]:
    if item == 2:
        list8.remove(item)
print(list8)

# （3）类似于其它语言里的 map
# 遍历 list8 里的每一个 item，如果 item 是奇数，那就把这个 item * 2 保留下来，最终返回一个数组
list88 = [item * 2 for item in list8 if item % 2 != 0]
print(list88)
