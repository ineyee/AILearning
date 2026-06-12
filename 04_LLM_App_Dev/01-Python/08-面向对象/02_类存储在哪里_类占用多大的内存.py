"""
用 class 定义的类，在 class 语句执行完成后，会生成一个类对象，类对象的数据类型都是 type
所以类也是存储在堆区的，以便将来解释器看到这些类就知道该怎么给它们的实例分配内存，类创建出来的对象也存储在堆区

至于类占用多大的内存主要取决于类的代码量，没有一个固定的值，也没有一个固定的计算方法
"""


class Person:
    age = 0


person = Person()

print(type(person))  # <class '__main__.Person'>
print(type(Person))  # <class 'type'>
print(type(type))  # <class 'type'>
