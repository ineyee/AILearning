"""
Python 里的类属性和对象属性比较奇葩

定义在类内部的属性就是类属性，可以通过类访问、也可以通过对象访问
而后续专门给对象添加的属性才是对象属性，只能通过对象访问
"""


class Person:
    # 这个属性就是类属性
    age = 0


person = Person()

print(Person.age)  # 0，通过类访问类属性
print(person.age)  # 0，通过对象访问类属性（对象访问属性时，其实是先找对象自己的属性，如果找不到就会去找所属类对象的同名属性）

# 这个属性就是对象属性，类里面没有，只有这个对象有，其它对象没有
person.height = 1.88
# 这个属性也是对象属性，其实不是在访问类属性，而是给这个对象新增了一个名字叫 age 的对象属性，因为我们明显可以看到 person.age 等于 18，但是 Person.age 还是等于 0
person.age = 18
print(person.height)  # 1.88，通过对象访问对象属性
print(person.age)  # 18
print(Person.age)  # 0
