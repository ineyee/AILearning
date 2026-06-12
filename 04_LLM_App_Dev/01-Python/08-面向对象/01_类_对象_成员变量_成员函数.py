# 用 class 关键字定义一个 Person 类，: 类似于其它语言里的 {}
class Person:
    # 属性/成员变量：其实就是变量封装在类里面，能直接初始化的就直接初始化掉，不能直接初始化或不方便初始化的就暂时赋值为 None
    name = None
    age = 0
    height = 0.5

    # 方法/成员函数：其实就是函数封装在类里面，只不过函数的第一个参数必须显示写个 self，使用其它成员时也必须显式写个 self
    def run(self):
        print("run()", self.name, self.age, self.height)


if __name__ == "__main__":
    # 创建一个 person 对象，无需 new 关键字
    person = Person()
    person.name = "张三"
    person.age = 18
    person.height = 1.88
    person.run()  # run() 张三 18 1.88
