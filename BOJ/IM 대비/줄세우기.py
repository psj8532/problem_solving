# 줄 세우기 # 11:32
n = int(input())

data = list(map(int,input().split()))
result = []
for i in range(1,n+1):
    if data[i-1]:
        result.insert(i-1-data[i-1],i)
    else:
        result.append(i)
print(*result)

#11:52