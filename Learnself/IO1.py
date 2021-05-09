#很多时候，数据读写不一定是文件，也可以在内存中读写。
#StringIO顾名思义就是在内存中读写str。
'''
如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
'''

#Python提供了pickle模块来实现序列化。
import pickle
d = dict(name='Bob', age=20, score=88)
d1=pickle.dumps(d) #pickle.dumps()方法把任意对象序列化成一个bytes
print(d1)

d = pickle.load() #pickle.loads()方法反序列化出对象

#json