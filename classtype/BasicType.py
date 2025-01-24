# -*- coding: utf-8 -*-
# 数字
from inherit.Case2 import Animal, Dog

class_int_type = type(123)
print(class_int_type) # <type 'int'>
print (class_int_type==int) # True, 表明该类型是数字类型，这里判断基本数据类型可以直接写int，str

# 字符串
class_str_type = type('this is willis')
print(class_str_type) # <type 'str'>
print(class_str_type==str) # True，表明该类型是字符串类型，这里判断基本数据类型可以直接写int，str

# None类型，是python中一个特殊的常量，用于表示空或不存在，类似于MENDIX中的empty
class_none_type = type(None)
print(class_none_type) # <type 'NoneType'>


import types

# 定义一个函数
def func():
    pass

def print_result(result):
    print("func result is: ", result)

# 我们来判断一下一个对象是否是函数
print_result(type(func) == types.FunctionType) # 用户自定义函数

print_result(type(abs) == types.BuiltinFunctionType) # 内置函数的类型
print_result(type(len) == types.BuiltinFunctionType)
print_result(type(max) == types.BuiltinFunctionType)

print_result(type(lambda x: x) == types.LambdaType)

print_result(type(x for x in range(10)) == types.GeneratorType)

"""对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数"""
"""【isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上】"""
"""例子见：inherit/Case2.py"""

"""比如，继承关系：object -> Animal -> Dog -> Husky"""
class Husky(Dog): # Husky即：哈士奇
    pass

animal = Animal()
dog = Dog()
husky = Husky()

result_case_1 = isinstance(husky,Husky);
print("husky is the instance of Class Husky?",result_case_1) # True, husky指的就是Husky类，是Husky new出来的对象

result_case_2 = isinstance(husky, Dog);
print("husky is the instance of Class Dog?",result_case_2) # True, husky同样也是Dog类的对象（husky也是狗），因为Dog是Husky的父类


result_case_3 = isinstance(husky, Animal);
print("husky is the instance of Class Animal?", result_case_3) # True, 同理，husky也是Animal

result_case_4 = isinstance(dog, Animal);
print("dog is  the instance of Class Animal?", result_case_4) # True, dog是Animal

result_case_5 = isinstance(dog, Husky);
print("dog is the instance of Class Husky?", result_case_5); # False, dog可不是Husky

"""能用type()判断的基本类型也可以用isinstance()判断"""
result_case_6 = isinstance('a', str)
print (result_case_6) # True
result_case_7 = isinstance(123, int)
print(result_case_7) # True
result_case_8 = isinstance(b'a', bytes)
print(result_case_8) # True

"""判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple"""
isinstance([1, 2, 3], (list, tuple)) # True, 是list
isinstance((1, 2, 3), (list, tuple)) # True, 是tuple


"""结论：总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”"""

