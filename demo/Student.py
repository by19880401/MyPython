

class Student(object):
    def __init__(self, name, age): # 相当于构造函数
        self.__name = name # 此处在self后边的name前加__，即name属性变为private [在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问]
        self.age = age


    def print_student_info(self):
        print("Name:", self.__name)
        print("Age:", self.age)




if __name__ == '__main__':
    student = Student("John", 18)
    student.print_student_info() # 可正常打印，因为它属于你调用student类的方法来间接地访问属性
    print(student.age) # 可正常打印
    print(student.name) # 私有属性不可访问，报错：AttributeError: 'Student' object has no attribute 'name'