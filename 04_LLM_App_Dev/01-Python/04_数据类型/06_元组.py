"""
Python 里的元组类似于数组，也可以用来定义一组数据，是不可变的
* 有序
* 元素可重复
* 可以存储不同类型的元素，并且实际开发中经常存放不同类型的元素
"""
tuple1 = ("张三", 18, 1.88)
print(tuple1)  # ('张三', 18, 1.88)
print(tuple1[0])  # 张三
print(tuple1[1])  # 18
print(tuple1[2])  # 1.88

# 元组常用来做解构赋值，一次性给多个变量赋值
tuple2 = ("张三", 18, 1.88)
name, age, height = tuple2
print(name)  # 张三
print(age)  # 18
print(height)  # 1.88


# 元组常用来做函数的返回值，实现多返回值的效果
def test():
    return "张三", 18, 1.88


tuple3 = test()
print(tuple3[0])  # 张三
print(tuple3[1])  # 18
print(tuple3[2])  # 1.88
