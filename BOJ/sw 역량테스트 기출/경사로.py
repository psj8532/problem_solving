def check_up(y,x):
    if x-L==0:
        return True
    elif x-L>0 and matrix[y][x-L-1]<=matrix[y][x-L]:
        return True
    else:
        return False

def check_down(y,x,v):
    for j in range(x+1,x+L):
        if x+L<=N and matrix[y][j] == v:
            continue
        else:
            return False
    else:
        if x+L == N:
            return N-1
        elif x+L < N and matrix[y][x+L-1] >= matrix[y][x+L]:
            return x+L-1
        else:
            return False

def check():
    global road
    for r in range(N):
        c = cnt = 1
        val = matrix[r][0]
        while c != N:
            if matrix[r][c] == val:
                cnt += 1
            elif val - matrix[r][c] == -1 and c == N - 1:
                if cnt >= L and check_up(r, c):  # 마지막 열일때, cnt를 확인안해서 틀렸음
                    pass
                else:
                    break
            elif val - matrix[r][c] == -1 and cnt >= L:
                if check_up(r, c):
                    cnt, val = 1, matrix[r][c]
                else:
                    break
            elif val - matrix[r][c] == 1:
                c = check_down(r, c, matrix[r][c])
                if c:
                    cnt, val = 0, matrix[r][c]
                else:
                    break
            else:
                break
            c += 1
        if c == N:
            road += 1

N,L = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
matrix_rotate = [[0]*N for _ in range(N)]
road = 0

check()
for j in range(N):
    for i in range(N):
        matrix_rotate[j][i]=matrix[i][j]
for i in range(N):
    for j in range(N):
        matrix[i][j] = matrix_rotate[i][j]
check()

print(road)

# def check_up(y,x):
#     if x-L==0:
#         return True
#     elif x-L>0 and matrix[y][x-L-1]<=matrix[y][x-L]:
#         return True
#     else:
#         return False
#
# def check_down(y,x,v):
#     for j in range(x+1,x+L):
#         if x+L<=N and matrix[y][j] == v:
#             continue
#         else:
#             return False
#     else:
#         if x+L == N:
#             return N-1
#         elif x+L < N and matrix[y][x+L-1] >= matrix[y][x+L]:
#             return x+L-1
#         else:
#             return False
#
# N,L = map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(N)]
# matrix_rotate = [[0]*N for _ in range(N)]
# road = 0
#
# for r in range(N):
#     c = cnt = 1
#     val = matrix[r][0]
#     while c!=N:
#         if matrix[r][c] == val:
#             cnt += 1
#         elif val-matrix[r][c]==-1 and c==N-1:
#             if cnt>=L and check_up(r,c): #마지막 열일때, cnt를 확인안해서 틀렸음
#                 pass
#             else:
#                 break
#         elif val-matrix[r][c]==-1 and cnt>=L:
#             if check_up(r,c):
#                 cnt,val = 1,matrix[r][c]
#             else:
#                 break
#         elif val-matrix[r][c]==1:
#             c = check_down(r,c,matrix[r][c])
#             if c:
#                 cnt,val = 0, matrix[r][c]
#             else:
#                 break
#         else:
#             break
#         c += 1
#     if c == N:
#         # print('{} right'.format(r))
#         road += 1
#
# for j in range(N):
#     for i in range(N):
#         matrix_rotate[j][i]=matrix[i][j]
#
# for i in range(N):
#     for j in range(N):
#         matrix[i][j] = matrix_rotate[i][j]
#
# for r in range(N):
#     c = cnt =1
#     val = matrix[r][0]
#     while c!=N:
#         if matrix[r][c] == val:
#             cnt += 1
#         elif val-matrix[r][c]==-1 and c==N-1:
#             if cnt>=L and check_up(r,c):
#                 pass
#             else:
#                 break
#         elif val-matrix[r][c]==-1 and cnt>=L:
#             if check_up(r,c):
#                 cnt,val = 1,matrix[r][c]
#             else:
#                 break
#         elif val-matrix[r][c]==1:
#             c = check_down(r,c,matrix[r][c])
#             if c:
#                 cnt,val = 0, matrix[r][c]
#             else:
#                 break
#         else:
#             break
#         c += 1
#     if c == N:
#         # print('{} down'.format(r))
#         road += 1
#
# print(road)