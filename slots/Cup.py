# -*- coding: utf-8 -*-
"""定义一个正常的Cup类，它没有任何属性"""
class Cup(object):
    pass

"""开始测试"""
cup = Cup()
cup.name = "I'm a Cup" # 动态给实例绑定一个属性
print(cup.name)

def set_cup_desc(self, desc):
    cup.desc = desc

from types import MethodType
cup.set_desc = MethodType(set_cup_desc,cup) # 给实例绑定一个方法

