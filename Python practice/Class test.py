class Animal(object):
    def run(self):
        print('running...')

class Dog(Animal):
    def run(self):
        print("Dog running...")

class Cat(Animal):
    def run(self):
        print("Cat running...")


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())

run_twice(Dog())


class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly...")

run_twice(Tortoise())


print(isinstance((1, 2, 3), (list, tuple)))
print(isinstance((1, 2, 3), (tuple)))
print(isinstance((1, 2, 3), (list)))
# 用isinstance来检查对象是否是某种type，可以检查是否存在于哪个类下

print(dir('ABC'))
# 所有没有用__XXX__标出的都可以直接用.XXX 来调用
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x + self.x

obj = MyObject()


hasattr(obj, 'x') # 有属性'x'吗？
# True
obj.x
# 9
hasattr(obj, 'y') # 有属性'y'吗？
# False
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') # 有属性'y'吗？
# True
getattr(obj, 'y') # 获取属性'y'
# 19
obj.y # 获取属性'y'
# 19

hasattr(obj, 'power') # 有属性'power'吗？
# True
getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn() # 调用fn()与调用obj.power()是一样的

getattr(obj, 'k', 404) #实际编码过程中，可以设置一个default值，如果属性不存在，就返回默认值

