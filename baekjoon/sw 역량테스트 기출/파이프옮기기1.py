import sys
sys.stdin = open("파이프옮기기1.txt","r")
from _collections import deque

def next_find_r(new_y,new_x,deq):
    global cnt
    if 0<=new_y<N and 0<=new_x+1<N and not matrix[new_y][new_x+1]:
        if (new_y,new_x+1)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y,new_x+1,0))
    if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
        if (new_y+1,new_x+1)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y+1,new_x+1,2))

def next_find_c(new_y,new_x,deq):
    global cnt
    if 0<=new_y+1<N and 0<=new_x<N and not matrix[new_y+1][new_x]:
        if (new_y+1,new_x)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y+1,new_x,1))
    if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
        if (new_y+1,new_x+1)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y+1,new_x+1,2))

def next_find_diag(new_y,new_x,deq):
    global cnt
    if 0<=new_y<N and 0<=new_x+1<N and not matrix[new_y][new_x+1]:
        if (new_y,new_x+1)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y,new_x+1,0))
    if 0<=new_y+1<N and 0<=new_x<N and not matrix[new_y+1][new_x]:
        if (new_y+1,new_x)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y+1,new_x,1))
    if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
        if (new_y+1,new_x+1)==(N-1,N-1):
            cnt += 1
            return
        deq.append((new_y+1,new_x+1,2))

def bfs(y,x,shape):
    deq = deque()
    deq.append((y,x,shape))

    while deq:
        here = deq.popleft()
        y,x,shape = here[0],here[1],here[2]
        if shape == 0:
            next_find_r(y,x,deq)
        elif shape == 1:
            next_find_c(y,x,deq)
        else:
            next_find_diag(y,x,deq)

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
bfs(0,1,0)
print(cnt)