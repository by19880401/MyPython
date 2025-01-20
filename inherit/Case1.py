# -*- coding: utf-8 -*-

class Animal(object): # 所有类都继承自objet
    def __init__(self):
        pass

    def eat(self):
        print("Animal is eating....")





class Cat(Animal):
    pass
class Dog(Animal):
    pass


cat = Cat()
cat.eat() # Animal is eating....
dog = Dog()
dog.eat() # Animal is eating....