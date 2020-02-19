# 색종이 # 20:58
import sys
sys.stdin = open("2563.text","r")

graph = [[0]*100 for _ in range(100)]
num = int(input())
for idx in range(num):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            graph[i][j] = 1
count=0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1:
            count+=1

print(count)
# 21:08