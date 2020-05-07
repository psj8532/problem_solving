import sys
sys.stdin = open("구슬탈출2.txt","r")
from _collections import deque
# 한킨씩 이동하는게 아니라 쭉 굴리는 것이다
# 구슬이 한 칸에 같이 있을 수 없다
# 10턴이 지나면 -1

def bfs(red,blue):
    ans = 0
    while red:
        here_r = red.popleft()
        ry,rx,d = here_r[0],here_r[1],here_r[2]
        if d>=10:
            return -1
        here_b = blue.popleft()
        by,bx = here_b[0],here_b[1]
        for dir in range(4):
            isRedExist = isBlueExist = isRed = isBlue= False
            new_ry,new_rx = ry+direct[dir][0],rx+direct[dir][1]
            new_by, new_bx = by + direct[dir][0], bx + direct[dir][1]
            while 0<=new_ry<N and 0<=new_rx<M and (matrix[new_ry][new_rx]=='.' or matrix[new_ry][new_rx] =='O') and not visited_r[new_ry][new_rx] and (new_ry,new_rx)!=(by,bx):
                if 0 <= new_ry < N and 0 <= new_rx < M and matrix[new_ry][new_rx] == 'O':
                    isRedExist = True
                    ans = d+1
                    ry = rx = -1
                    break
                new_ry,new_rx = new_ry+direct[dir][0],new_rx+direct[dir][1]
                isRed = True
            new_ry,new_rx = new_ry-direct[dir][0],new_rx-direct[dir][1]

            while 0 <= new_by < N and 0 <= new_bx < M and (
                    matrix[new_by][new_bx] == '.' or matrix[new_by][new_bx] == 'O') and not visited_b[new_by][new_bx] and (new_ry, new_rx) != (new_by, new_bx):
                if 0 <= new_by < N and 0 <= new_bx < M and matrix[new_by][new_bx] == 'O':
                    isBlueExist = True
                isBlue = True
                new_by, new_bx = new_by + direct[dir][0], new_bx + direct[dir][1]
            new_by,new_bx = new_by-direct[dir][0],new_bx-direct[dir][1]
            #빨간색o,파란색o #빨간색x,파란색o
            if (isRedExist and isBlueExist) or (not isRedExist and isBlueExist):
                return -1
            #빨간색o,파란색x
            elif isRedExist and not isBlueExist:
                return ans
            #빨간색x,파란색x
            else:
                #빨간경로o,파란경로o
                red.append((new_ry,new_rx,d+1))
                blue.append((new_by,new_bx))
                visited_r[new_ry][new_rx] = 1
                visited_b[new_by][new_bx] = 1
                #빨간경로o,파란경로x
                red.append((new_ry,new_rx,d+1))
                blue.append((by,bx))
                visited_r[new_ry][new_rx] = 1
                #빨간경로x,파란경로o
                red.append((ry,rx,d+1))
                blue.append((new_by,new_bx))
                visited_b[new_by][new_bx] = 1
                #빨간경로x,파란경로x
                #pass
    return -1



direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
visited_b = [[0]*M for _ in range(N)]
visited_r = [[0]*M for _ in range(N)]
red = deque()
blue = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j]=='R':
            visited_r[i][j] = 1
            red.append((i,j,0))
        elif matrix[i][j]=='B':
            visited_b[i][j] = 1
            blue.append((i,j))
result = bfs(red,blue)
print(result)

# def bfs(red,blue):
#     cnt_r = cnt_b = 1
#     count_r = count_b = 0
#     while cnt_r:
#         while cnt_b:
#             here = blue.popleft()
#             y,x = here[0],here[1]
#             cnt_b -= 1
#             for dir in range(4):
#                 new_y,new_x = y+direct[dir][0],x+direct[dir][1]
#                 if matrix[new_y][new_x]=='O':
#                     return -1
#                 elif matrix[new_y][new_x]=='.' and not visited_b[new_y][new_x]:
#                     blue.append((new_y,new_x))
#                     count_b += 1
#         while cnt_r:
#             here = red.popleft()
#             y, x, d = here[0], here[1], here[2]
#             cnt_r -= 1
#             for dir in range(4):
#                 new_y, new_x = y + direct[dir][0], x + direct[dir][1]
#                 if matrix[new_y][new_x] == 'O':
#                     return d+1
#                 elif matrix[new_y][new_x] == '.' and not visited_r[new_y][new_x] and not (new_y,new_x) in blue:
#                     red.append((new_y, new_x, d + 1))
#                     count_r += 1
#         cnt_r,cnt_b = count_r,count_b
#         count_r = count_b = 0
#     return -1
#
# direct = [(-1,0),(0,1),(1,0),(0,-1)]
# N,M = map(int,input().split())
# matrix = [list(input()) for _ in range(N)]
# visited_b = [[0]*M for _ in range(N)]
# visited_r = [[0]*M for _ in range(N)]
# red = deque()
# blue = deque()
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j]=='R':
#             visited_r[i][j] = 1
#             red.append((i,j,0))
#         elif matrix[i][j]=='B':
#             visited_b[i][j] = 1
#             blue.append((i,j))
# result = bfs(red,blue)
# print(result)
