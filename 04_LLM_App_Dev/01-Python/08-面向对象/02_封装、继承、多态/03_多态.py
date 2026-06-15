"""
多态是指子类重写父类的方法、然后“父类指针”指向子类对象、然后用“父类指针”调用子类重写的方法，不同的子类就会产生不同的执行结果
"""


class Animal:
    def run(self):
        print("Animal run")


class Cat(Animal):
    def run(self):
        print("Cat run")


class Dog(Animal):
    def run(self):
        print("Dog run")


animal = Animal()
animal1 = Cat()
animal2 = Dog()

animal.run()  # Animal run
animal1.run()  # Cat run
animal2.run()  # Dog run
