# -*- coding: utf-8 -*-
"""可以给类的实例绑定任何属性和方法，这就是动态语言的灵活性，但slots会限制实例绑定属性，demo here"""

"""定义一个正常的Cup类，它没有任何属性"""
class Cup(object):
    __slots__ = ("name", "age") # 定义允许绑定的属性名称
    pass

"""*****开始测试*****"""
cup_shadow = Cup()
cup_shadow.name = "I'm a Cup" # 动态给实例绑定一个属性
print(cup_shadow.name) # 打印结果：I'm a Cup

cup_shadow.age = 36
print(cup_shadow.age)

cup_shadow.desc = "this is a desc for cup shadow" # 不允许添加，会报错
print(cup_shadow.desc) # 报错: AttributeError: 'Cup' object has no attribute 'desc'


"""__slots__定义的属性仅对当前类实例起作用,对继承的子类是不起作用的,除非在子类中也定义__slots__"""







