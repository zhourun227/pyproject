#python所有变量均为引用类型
#浮点数精度的问题,可以导入decimal(十进制的)模块
#is用于判断两个变量的引用是否为同一个对象，而==用于判断变量引用的对象的值是否相等！
#id()，用它可以查看某个变量或者对象的内存地址，两个相同内存地址的对象被认为是同一个对象。

#input函数的返回值是一个字符串类型
age=input("请输入:")
print(type(age))  #str
age=(int)(age)   ## 使用isdigit函数判断输入是否全是数字格式
print(type(age))  #int

#print函数的原型：print(self, *args, sep=' ', end='\n', file=None)
print("我叫%s,今年%d岁" % ("小米",10))
tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')#String.format

#del是Python的删除关键字，可以删除变量、函数、类等等。
bool(1)#内置的bool()函数可以用来测试一个表达式的布尔值结果
#None也不是布尔类型，而是NoneType。


lis=[1,2,3,4,5]
print(lis[0])
lis[0]='s'
lis.remove(2)#删除的是内容
lis.pop(2)#删除的是下标对应的元素
lis[1:4:2]  #Start:end:
lis[-1:-3:1]
#有很多属性

#元组:内容不可变的列表
#元组只保证它的一级子元素不可变，对于嵌套的元素内部，不保证不可变！
tup = ('a', 'b', ['A', 'B'])
tup[2][0] = 'X'
tup[2][1] = 'Y'
print(tup)

#字典
dic = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dic['Beth'])
dic['address']='shanghai'
dic['address']='chrengdu'
print(dic['address'])
dic.pop('Cecil')
#del dic['Cecil']
#同时遍历key,value...
for key,value in dic.items():
    print(key,value)

s={1,2,3,3,3}
print(s)


#函数,面向对象，正则表达式
def fun1(x):
    pass
def fun2(x,y=1): #必选参数在前，默认参数在后
    pass
def fun3(x,n):
    pass
def fun4(*num):
    pass

with open("","w","a") as  f:  #with直接省略close
    print(f)
