age = 20
if age >= 6:
    print('teenager')   #如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
elif age >= 18:
    print('adult')
else:
    print('kid')

#input()返回的数据类型是str,需要强转
'''
il=input('请输入数字:')
i=int(il)
'''

names = ['Michael', 'Bob', 'Tracy']
for name in names:  #依次把list或tuple中的每个元素迭代出来
    print(name)

print(list(range(5)))
sum = 0
for x in range(101):  #可以生成一个整数序列
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:            #true
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)