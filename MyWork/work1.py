class Test:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def ceshi(self):
        print("名字",self.name,end=',')
        print("年龄:",self.age,",","性别:",self.sex)
a=Test("周润",20,"男")
a.ceshi()
lis=["wo","ai",5]
for i in lis:
    print(i,end=",")
print(lis[0:2])
lis.append("zhourun")
for k in lis:
    print(k,end=',')
lis.remove("wo")
for k in lis:
    print(k,end=',')
print("----------------------------------->")
for i in range(10):
    print(i)
a=['Google', 'Baidu', 'Huawei', 'Taobao', 'QQ']
for i in range(len(a)):
    print(a,a[i])
print("---------------------------------->")
for i in range(1,10,1):
    for j in range(9,0,-1):
        print(j,"*",i,"=",j*i)
        print()
print("------------------------------------>")
n=10
sum = 0
counter = 1
while(counter<=n):
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))