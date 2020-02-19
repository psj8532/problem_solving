#직사각형 네개의 합집합의 면적 구하기 #21:25
import sys
sys.stdin = open("2669.text","r")


graph = [[0]*100 for _ in range(100)]

count = 0


for num in range(4):
    rect = list(map(int,input().split()))
    for i in range(rect[0],rect[2]):
        for j in range(rect[1],rect[3]):
            graph[i][j] = 1

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            count+=1
print(count)

#21:37 종료