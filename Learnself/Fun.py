a=abs(-20) #注意传入参数
print(a)

#数据类型转换
int('123')
float('12.34')
str(1.23)
str(100)
bool(1)
bool('')

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

#返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(100, 100, 60, math.pi / 6)) #返回值是一个tuple,其实还是一个值


def power(x, n):  #位置参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,2))

def power(x, n=2): #默认参数  必选参数在前，默认参数在后
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))  #也可以传入n

def add_end(L=[]):     # 定义默认参数要牢记一点：默认参数必须指向不变对象！
    L.append('END')
    return L
print(add_end())
print(add_end())  #数组是可变对象

def calc(*numbers): #可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2))
print(calc(1))

#关键字参数,命名关键字参数.见参考！
 
#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
#尾递归 解决递归调用栈溢出
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))