"""
静态方法是指用 @staticmethod 或 @classmethod 修饰的方法，可以用“类名.静态方法”的方式来访问

1、@staticmethod：真正的静态方法，不会自动接收类对象
2、@classmethod：类方法，会自动接收当前类对象作为第一个参数，通常命名为 cls
"""


class Person:
    @staticmethod
    def run():
        print("run")

    @classmethod
    def eat(cls):
        print("eat")


Person.run()  # run
Person.eat()  # eat
