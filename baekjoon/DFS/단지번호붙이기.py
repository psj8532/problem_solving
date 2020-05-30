# for문으로 1인 곳 탐지 -> 그 곳부터 델타를 이용하여 1인 곳 번호 매겨가기
# 하나의 단지가 탐지 완료되면 단지내 집의 수를 리스트에 추가
#  다른 1 탐지
#스택
def dfs(y,x,cnt):
    stack = []
    stack.append((y,x))

    while stack:
        here = stack.pop()
        y,x = here[0],here[1]
        if not visited[y][x]:
            visited[y][x] = 1
            cnt += 1
        else: continue
        for dir in range(3,-1,-1):
            new_y,new_x = y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<n and 0<=new_x<n and matrix[new_y][new_x] and not visited[new_y][new_x]:
                stack.append((new_y,new_x))
    return cnt
n = int(input())
matrix = [list(map(int,input())) for _ in range(n)]
direct = [(-1,0),(0,1),(1,0),(0,-1)]
result = []
visited = [[0]*n for _ in range(n)]
num = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] and not visited[i][j]:
            count = dfs(i,j,0)
            result.append(count)
            num += 1

result.sort()
print(num)
for i in range(len(result)):
    print(result[i])

#재귀
# def complex(y,x):
#     global cnt
#     matrix[y][x]=0
#     for dir in range(len(dy)):
#         new_y = y+dy[dir]
#         new_x = x+dx[dir]
#         if 0<=new_y<n and 0<=new_x<n and matrix[new_y][new_x]==1:
#             matrix[new_y][new_x]=0
#             cnt+=1
#             complex(new_y,new_x)
#     return cnt
#
# n=int(input())
# matrix=[]
# dy=[-1,0,1,0]
# dx=[0,1,0,-1]
# result = []
# for _ in range(n):
#     matrix.append(list(map(int,input())))
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j]==1:
#             cnt=1
#             temp = complex(i,j)
#             result.append(temp)
#
# result.sort()
# print(len(result))
# for i in range(len(result)):
#     print(result[i])
#21:27