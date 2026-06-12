"""
1、为什么需要 self 指针

上面我们说到“成员变量的值存储在对象内部，成员函数存储在对象外部的堆区”，也就是说下面的代码中"张三"存储在 person 对象内部、"李四"存储在 person1 对象内部，run 成员函数存储在堆区只有一份
那么问题来了，既然 run 成员函数不存储在 person 对象和 person1 对象内部，那 run 成员函数执行体里是怎么知道 person 对象调用的时候就打印"张三"、person1 对象调用的时候就打印"李四"的呢
也就是说堆区的 run 到底是怎么访问到 person、person1 这两块栈区的内存的呢

其实编译器会为每个成员函数都添加一个参数——self 指针——并且这个参数永远位于参数列表的第一位
外界某个对象通过点语法调用成员函数这种高级语言里的写法，在编译的时候编译器其实就是把外界这个对象的内存地址传递给了成员函数的 self 指针，于是 self 指针就指向了成员函数的调用者
因此我们就可以在成员函数执行体里通过 self 指针来访问某个具体对象的成员变量、成员函数了，所有的面向对象语言里对象调用成员函数都是这么设计的

2、Python 里的 self 必须显式写出来
"""


class Person:
    name = None

    def run(self):
        print(self.name, "run")


person = Person()
person.name = "张三"
person.run()  # 张三 run

person1 = Person()
person1.name = "李四"
person1.run()  # 李四 run
