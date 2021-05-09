f = abs
print(f)
a=f(-10)  #函数本身也可以赋值给变量,即：变量可以指向函数。
print(a)

#函数名也是变量
#abs = 10 #abs指向10

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)
print(add(-5,6,abs))

#Python内建了map()和reduce()函数
def f(x):
    return x*x
r=(map(f,[1,2,3,4,5,6,7,8,9]))  #map()函数接收两个参数，一个是函数，一个是Iterable
print(list(r))

from functools import reduce
def f(x,y):
    return x * 10 + y
reduce(f, [1, 3, 5, 7, 9])

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'])

#函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())
#闭包

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
l=list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

