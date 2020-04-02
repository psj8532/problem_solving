def func(a,b=1,c=2,*args,**kwargs):
    d=sum([n*2 for n in args if n>2])
    e=sum([v**2 for v in kwargs.values()])
    return a+b+c+d+e

print(func(2,4,6,1,3,5,x=2,y=3))