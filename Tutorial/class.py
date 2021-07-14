class Animal:
    def run(self):
        print("running")


class Dog(Animal):
    def __init__(self, habbit):
        self.habbit = habbit

    def eat(self):
        print("eating")


class Cat(Animal):
    pass


dog1 = Dog("eat")
dog2 = Dog("run")

dog1.run()
dog2.run()

print(dog1.habbit, dog2.habbit)

#
# book
# 属性
# author
# public date
# name
# ISBN

class book:
    def __init__(self, author, public_date, name, ISBN=None):
        self.author = author
        self.public_date = public_date
        self.name = name
        self.ISBN = ISBN

