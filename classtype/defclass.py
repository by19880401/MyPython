# -*- coding: utf-8 -*-

"""Python是动态语言，根据类创建的实例可以任意绑定属性"""
class Seagate(object):
    def __init__(self, name):
        self.name = name # 有一个name属性，此时，看起来跟Java类型


"""start to test"""
seagate = Seagate("seagate")
seagate.score = 90 # 这里就牛B了，明明没有score属性，活生生地给“造”出来这样一个属性
print(seagate.name)
has_score = hasattr(seagate, "score")
print("has score?", has_score)
print(seagate.score)


