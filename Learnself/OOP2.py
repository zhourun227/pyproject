class Student(object):
    __slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称,限制该class实例能添加的属性
s=Student()
s.name = 'Michael'
s.age = 25
#s.score = 99  #不能添加

#Python允许使用多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
# 各种动物:
class Dog(Mammal,Runnable):  #多重继承,这种设计通常称之为MixIn。
    pass
class Bat(Mammal,Bird):
    pass

#定制类
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

#使用枚举类
from enum import Enum, unique
#每个常量都是class的一个唯一实例
@unique #装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
w=Weekday.Mon
w1=Weekday.Mon.value
print(w,w1)