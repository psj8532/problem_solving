n=int(input())
data=list(map(int,input().split()))
b,c=map(int,input().split())
result=0
for i in range(n):
    result+=1
    if data[i]-b>0:
        temp=data[i]-b
        if temp%c:
            result=result+(temp//c+1)
        else:
            result=result+(temp//c)
print(result)