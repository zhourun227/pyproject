d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Adam'] = 67
print(d)
#要避免key不存在的错误，有两种办法
b='Thomas' in d
print(b)
print(d.get('Thomas'))#通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
c=d.pop('Bob') #要删除一个key，用pop(key)方法
print(c)
print(d)

s = set([1,2,3])#要创建一个set，需要提供一个list作为输入集合
print(s)
s.add(4)
s.remove(4)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2