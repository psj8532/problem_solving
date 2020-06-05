import sys
sys.stdin = open("파이프옮기기1.txt","r")
from _collections import deque

def next_find_r(new_y,new_x,deq,shape):
    global cnt
    if 0<=new_y<N and 0<=new_x+1<N and not matrix[new_y][new_x+1]:
        if (new_y,new_x+1)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y][new_x+1] and (new_y,new_x+1,shape) in deq:
                count_list[new_y][new_x+1] += count_list[new_y][new_x]
            else:
                deq.append((new_y,new_x+1,0))
                count_list[new_y][new_x+1] =1
    if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
        if (new_y+1,new_x+1)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y+1][new_x + 1]:
                count_list[new_y+1][new_x + 1] += count_list[new_y][new_x]
            else:
                deq.append((new_y+1, new_x + 1, 2))
                count_list[new_y+1][new_x+1] = 1
def next_find_c(new_y,new_x,deq,shape):
    global cnt
    if 0<=new_y+1<N and 0<=new_x<N and not matrix[new_y+1][new_x]:
        if (new_y+1,new_x)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y+1][new_x]:
                count_list[new_y+1][new_x] += count_list[new_y][new_x]
            else:
                deq.append((new_y+1, new_x, 1))
                count_list[new_y+1][new_x] = 1
    if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
        if (new_y+1,new_x+1)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y+1][new_x + 1]:
                count_list[new_y+1][new_x + 1] += count_list[new_y+1][new_x+1]
            else:
                deq.append((new_y+1, new_x + 1, 2))
                count_list[new_y+1][new_x+1] = 1

def next_find_diag(new_y,new_x,deq,shape):
    global cnt
    if 0<=new_y<N and 0<=new_x+1<N and not matrix[new_y][new_x+1]:
        if (new_y,new_x+1)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y][new_x + 1]:
                count_list[new_y][new_x + 1] += count_list[new_y][new_x]
            else:
                deq.append((new_y, new_x + 1, 0))
                count_list[new_y][new_x+1] = 1
    if 0<=new_y+1<N and 0<=new_x<N and not matrix[new_y+1][new_x]:
        if (new_y+1,new_x)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y+1][new_x]:
                count_list[new_y+1][new_x] += count_list[new_y][new_x]
            else:
                deq.append((new_y+1, new_x, 1))
                count_list[new_y+1][new_x] = 1
    if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
        if (new_y+1,new_x+1)==(N-1,N-1):
            cnt += count_list[new_y][new_x]
            return
        else:
            if count_list[new_y+1][new_x + 1]:
                count_list[new_y+1][new_x + 1] += count_list[new_y][new_x]
            else:
                deq.append((new_y+1, new_x + 1, 2))
                count_list[new_y+1][new_x+1] = 1

def bfs(y,x,shape,count):
    deq = deque()
    deq.append((y,x,shape,count))
    count_list[y][x] = 1
    while deq:
        here = deq.popleft()
        y,x,shape = here[0],here[1],here[2]
        if shape == 0:
            next_find_r(y,x,deq,shape)
        elif shape == 1:
            next_find_c(y,x,deq,shape)
        else:
            next_find_diag(y,x,deq,shape)

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
count_list = [[0]*N for _ in range(N)]
cnt = 0
bfs(0,1,0,1)
print(cnt)

# def next_find_r(new_y,new_x,deq):
#     global cnt
#     if 0<=new_y<N and 0<=new_x+1<N and not matrix[new_y][new_x+1]:
#         if (new_y,new_x+1)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y,new_x+1,0))
#     if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
#         if (new_y+1,new_x+1)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y+1,new_x+1,2))
#
# def next_find_c(new_y,new_x,deq):
#     global cnt
#     if 0<=new_y+1<N and 0<=new_x<N and not matrix[new_y+1][new_x]:
#         if (new_y+1,new_x)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y+1,new_x,1))
#     if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
#         if (new_y+1,new_x+1)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y+1,new_x+1,2))
#
# def next_find_diag(new_y,new_x,deq):
#     global cnt
#     if 0<=new_y<N and 0<=new_x+1<N and not matrix[new_y][new_x+1]:
#         if (new_y,new_x+1)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y,new_x+1,0))
#     if 0<=new_y+1<N and 0<=new_x<N and not matrix[new_y+1][new_x]:
#         if (new_y+1,new_x)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y+1,new_x,1))
#     if 0<=new_y+1<N and 0<=new_x+1<N and not matrix[new_y][new_x+1] and not matrix[new_y+1][new_x] and not matrix[new_y+1][new_x+1]:
#         if (new_y+1,new_x+1)==(N-1,N-1):
#             cnt += 1
#             return
#         deq.append((new_y+1,new_x+1,2))
#
# def bfs(y,x,shape):
#     deq = deque()
#     deq.append((y,x,shape))
#
#     while deq:
#         here = deq.popleft()
#         y,x,shape = here[0],here[1],here[2]
#         if shape == 0:
#             next_find_r(y,x,deq)
#         elif shape == 1:
#             next_find_c(y,x,deq)
#         else:
#             next_find_diag(y,x,deq)
#
# N = int(input())
# matrix = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# bfs(0,1,0)
# print(cnt)