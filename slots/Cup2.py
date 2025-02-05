# -*- coding: utf-8 -*-
"""可以给类的实例绑定任何属性和方法，这就是动态语言的灵活性，但slots会限制实例绑定属性，demo here"""

"""定义一个正常的Cup类，它没有任何属性"""
class Cup(object):
    __slots__ = ("name", "age") # 用tuple定义允许绑定的属性名称
    pass

"""*****开始测试*****"""
cup = Cup()
cup.name = "I'm a Cup" # 动态给实例绑定一个属性
print(cup.name) # 正常case，打印结果：I'm a Cup

def set_cup_desc(self, desc): # 定义一个方法
    cup.desc = desc

from types import MethodType
cup.set_desc = MethodType(set_cup_desc,cup) # 动态给给实例绑定这个方法
cup.set_desc("I'm the description for Cup.") #调用该方法
print(cup.desc) # 正常case，打印结果：I'm the description for Cup.

"""注意：给一个实例绑定的方法，对另一个实例是不起作用的，如果所有实例都需要该方法，才此方法直接定义在类中即可"""

cup2 = Cup()
cup2.set_desc("cup2 description") # 报错






