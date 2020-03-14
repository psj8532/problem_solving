number = 123
temp = number
num = [0]*3
cnt=0

while temp:
    cnt+=1
    temp//=10
temp = number

for i in range(cnt-1,-1,-1):    
    num[i] = temp % 10 
    temp //= 10
print(num)