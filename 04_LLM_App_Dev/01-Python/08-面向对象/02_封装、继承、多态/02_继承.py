"""
一、继承是指子类拥有了父类所有的属性、方法、静态属性、静态方法，在子类名后面写 (父类名) 即可

注意：Python 里所有的类最终都继承自基类 object
也就是说下面的 Person 类其实就继承自 object：class Person(object): ...
只不过已经默认了，我们不需要显性地写出来继承自 object 而已
"""


class Person:
    age = 0

    def run(self):
        print(f"run() {self.age}")


class Student(Person):
    pass


person = Person()
person.age = 18
person.run()  # run() 18

student = Student()
student.age = 14
student.run()  # run() 18

"""
二、构造方法的补充

1、如果子类不重写父类的构造方法，是没有问题的，创建子类的时候无非是默认调用父类的构造方法，就像上面的 Person 和 Student 那样
2、如果子类有自己的构造方法——即重写了父类的构造方法，那子类的构造方法里就必须在第一行首先调用一下 super().__init__() 方法————即父类的构造函数，来完成子类继承于父类那部分资源的初始化，然后再做子类自己自定义的内容
"""


class Person0201:
    def __init__(self, age):
        self.age = age

    age = 0

    def run(self):
        print(f"run() {self.age}")


class Student0201(Person0201):
    no = 0

    def __init__(self, no):
        super().__init__(0)

        self.no = no


"""
三、方法的重写和调用父类的方法

1、Python 里子类重写父类的方法直接重写就行，不用加 @override 之类的修饰
2、那重写之后怎么调用父类的方法呢？Python 里有 super() 关键字来调用父类的方法
"""


class Person0202:
    def run(self):
        print("Person0202 run()")


class Student0202(Person0202):
    def run(self):
        super().run()

        print("Student0202 run()")


"""
四、super() 关键字

1、super() 关键字出现在子类的构造方法里时，代表的是调用父类的构造方法
2、super() 关键字出现在子类的实例方法里时，代表的是调用父类的同名方法
3、super() 关键字出现在子类的类方法里时，代表的是调用父类的同名方法
"""
