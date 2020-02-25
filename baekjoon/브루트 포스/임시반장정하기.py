#1268 #19:42
import sys
sys.stdin=open("임시반장정하기.text","r")

n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
count_list = [[0]*5 for _ in range(n)]

for student in range(n):
    visited = [0] * n
    for grade in range(5):
        for comp in range(n):
            if student!=comp and data[student][grade]==data[comp][grade] and not visited[comp]:
                count_list[student][grade]+=1
                visited[comp]=1
result=[]
for y in range(n):
    cnt=0
    for x in range(5):
        cnt+=count_list[y][x]
    result.append(cnt)

max_val = -1
for i in range(len(result)):
    if max_val<result[i]:
        max_val= result[i]
        max_idx = i
print(max_idx+1)