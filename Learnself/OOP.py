class Student(object):

    def __init__(self, name, score):
        self.__name = name  #私有变量
        self.__score = score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

stu=Student('zr',20)
print(stu.print_score())

#实例属性和类属性
stu.age=20   #只适用于当前实例
Student.age=19