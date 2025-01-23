# -*- coding: utf-8 -*-

class Animal(object): # 所有类都继承自objet
    def __init__(self):
        pass

    def eat(self):
        print("Animal is eating....")





class Cat(Animal):
    def eat(self):
        print("Cat is eating....") # 覆盖eat()方法，子类自定义自己的eat()逻辑
    def run(self):
        print("Cat is running....")
class Dog(Animal):
    def eat(self):
        print("Dog is eating....")


cat = Cat()
cat.eat() # Cat is eating....
cat.run() # Cat is running....
dog = Dog()
dog.eat() # Dog is eating....


"""判断数据类型"""
a = list() # list类型
b = Animal()
c = Cat()

result_a = isinstance(a, list)
print(result_a) # True，a是list类型
result_b = isinstance(b, Animal)
print(result_b) # True，b是Animal类型
result_c = isinstance(c, Cat)
print(result_c) # True, c是Cat类型

result_cc = isinstance(c, Animal)
print(result_cc) # True, c也是Animal类型

result_bb = isinstance(b, Cat)
print(result_bb) # False, b Animal却不是Cat类型


