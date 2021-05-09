class tt:
    def reverseLeftWords(self):
        lis=["abcdefg","ccc"]
        for i in range(len(lis)):
            print(i,lis[i])
t=tt()
t.reverseLeftWords()

class slo:
    def numberOfSteps (num:int):
        m=0
        while(num!=0):
            if num%2==0:
                num=num/2
                m=m+1
            else:
                num=(num-1)
                m=m+1
            print(m)


s=slo
s.numberOfSteps(14)


