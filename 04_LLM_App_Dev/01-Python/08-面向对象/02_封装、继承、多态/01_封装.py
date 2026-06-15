"""
我们把众多变量和函数都放到一个类里，将来通过类和对象来访问这些变量和函数，而不再是零散地独立地访问众多变量和函数，这可以称之为封装

通常情况下，我们还会把属性私有化，然后提供公开的setter方法和getter方法供外界访问属性
"""


class Person:
    _age = 0

    # @property 可以把一个方法变成 getter 方法
    # getter 方法内部访问的是 self._age 而不是 self.age，所以不会死循环
    @property
    def age(self):
        return self._age

    # @age.setter 可以把一个方法变成 setter 方法
    # setter 方法内部访问的是 self._age 而不是 self.age，所以不会死循环
    @age.setter
    def age(self, age):
        if age < 0:
            self._age = 0
        else:
            self._age = age


person = Person()
person.age = -10
print(person.age)
