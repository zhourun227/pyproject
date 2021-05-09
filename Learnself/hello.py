print(r'''
\r,\n
''')
True & True
#字符编码

#列表
classmates = ['Michael', 'Bob', 'Tracy',0,[1,2,3],(11,11),True]
a=classmates[4][1];
b=classmates[-1]
classmates.append('adam')  #可以往list中追加元素到末尾
classmates.insert(1, 'Jack')
classmates.pop(1)  #删除下标
classmates.remove("Bob")  #删除元素
classmates[1] = 'Sarah'  #元素替换
print(a)
print(b)
print(len(classmates))

#元组
classmates = ('Michael', 'Bob', 'Tracy')
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t=(1,)
t = ('a', 'b', ['A', 'B'])
t[2][0]='X'
print(t)

import sklearn