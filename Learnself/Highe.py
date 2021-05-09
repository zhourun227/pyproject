L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3] #Python提供了切片（Slice）操作符,左闭右开
L[:3]
L[-2:] #倒数第一个元素的索引是-1

l=[range(100)] #[0, 1, 2, 3, ..., 99]
l[:10:2]
L[:] #只写[:]就可以原样复制一个list

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
(0, 1, 2, 3, 4, 5)[:3]

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符
'ABCDEFG'[:3]  #'ABC'
'ABCDEFG'[::2]  #'ACEG'

#迭代（Iteration）
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,value)

#判断一个对象是可迭代对象
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代

#list实现类似Java那样的下标循环,enumerate(列举)函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

#列表生成式即List Comprehensions,多用于对列表操作
a=[x * x for x in range(1, 11) if x % 2 == 0] #不能在最后的if加上else,因为跟在for后面的if是一个筛选条件
print(a)
b=[x if x % 2 == 0 else -x for x in range(1, 11)] #for前面的部分是一个表达式，它必须根据x计算出一个结果
print(b)

#生成器：generator。只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))  #不能直接打印
#next(g)  #，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
for n in g:
    print(n)

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator!



