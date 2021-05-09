class jc:
    def jiecheng(x):
        if x==1:
            return 1
        else:
            return x*jc.jiecheng(x-1)

    def jiecheng1(x):
        res=1
        y=x
        while(y>=0):
            res=res*y
            y=y-1
        return res
j=jc
print(j.jiecheng(5))
print(j.jiecheng1(5))

