#08:49
n=int(input())
# result = (n-1)*(10**3)+666
# print(result)
cnt=0
num=666
while cnt!=n:
    num=str(num)
    for idx in range(len(num)-2):
        if num[idx]=='6' and num[idx+1]=='6' and num[idx+2]=='6':
            cnt+=1
            result = int(num)
            break
    num=int(num)
    num+=1
print(result)
#09:15