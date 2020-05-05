import sys
sys.stdin = open("탈출.txt", "r")
from _collections import deque

def bfs(sy,sx,gy,gx,d,water):
    global cnt_w
    schrenk = deque()
    schrenk.append((sy,sx,d))
    count_w = count_s = 0
    cnt_s = 1

    while schrenk: #고슴도치가 나중에 이동하므로 물이 다 찼아도 마지막에 고슴도치가 이동할 기회는 줘야함
        while cnt_w:
            here_w = water.popleft()
            wy,wx = here_w[0],here_w[1]
            cnt_w -= 1
            for dir in range(4):
                new_wy, new_wx = wy + direct[dir][0], wx + direct[dir][1]
                if 0 <= new_wy < r and 0 <= new_wx < c and matrix[new_wy][new_wx] != 'X' and matrix[new_wy][new_wx] != 'D' and not visited_w[new_wy][new_wx]:
                    water.append((new_wy, new_wx))
                    visited_w[new_wy][new_wx] = 1
                    count_w += 1
        while cnt_s:
            here = schrenk.popleft()
            y,x,d = here[0],here[1],here[2] #고슴도치 이동이 끝났을때 cnt = count
            cnt_s -= 1
            for dir in range(4):
                new_y,new_x = y+direct[dir][0],x+direct[dir][1]
                if 0<= new_y<r and 0<=new_x<c and matrix[new_y][new_x]=='D':
                    return d+1
                elif 0<=new_y<r and 0<=new_x<c and matrix[new_y][new_x]=='.' and not visited_s[new_y][new_x] and not visited_w[new_y][new_x]:
                    schrenk.append((new_y,new_x,d+1))
                    visited_s[new_y][new_x] = 1
                    count_s += 1
        cnt_w,cnt_s = count_w,count_s
        count_w = count_s = 0
    return False

direct = [(-1,0),(0,1),(1,0),(0,-1)]
r,c = map(int,input().split())
matrix = [list(input()) for _ in range(r)]
visited_w = [[0]*c for _ in range(r)]
visited_s = [[0]*c for _ in range(r)]
water = deque()
cnt_w = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j]=='D':
            gy,gx = i,j
        elif matrix[i][j]=='S':
            sy,sx = i,j
            visited_s[i][j] = 1
        elif matrix[i][j] == '*':
            water.append((i,j))
            visited_w[i][j] = 1
            cnt_w += 1

result = bfs(sy,sx,gy,gx,0,water)
if result:
    print(result)
else:
    print('KAKTUS')