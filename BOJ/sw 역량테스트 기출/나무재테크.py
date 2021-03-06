from _collections import deque

dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,1,1,1,0,-1,-1,-1]
answer = 0
N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
tree = {(i,j): deque() for i in range(N) for j in range(N)}
for i in range(M):
    x, y, z = map(int,input().split())
    tree[(x-1,y-1)].append(z)
matrix = [[5] * N for _ in range(N)]
time = 0
while time < K:
    # print('시작')
    # for row in martix:
    #     print(*row)
    # 봄
    for k in tree.keys():
        # tree[k].sort()
        r, c = k
        survived_tree = deque()
        val = 0
        for age in tree[k]:
            if matrix[r][c] - age >= 0:
                matrix[r][c] -= age
                survived_tree.append(age+1)
            else:
                val += age // 2
        tree[k] = survived_tree
        matrix[r][c] += val
    # print('봄')
    # for row in martix:
    #     print(*row)
    # print('산 나무: ',)
    # for k,lst in tree.items():
    #     print(k,lst)
    # print('죽은 나무: ')
    # for k,lst in died_tree.items():
    #     print(k,lst)
    # 여름
    # print('여름')
    # for row in martix:
    #     print(*row)
    # 가을
    temp = {(i,j): 0 for i in range(N) for j in range(N)}
    for k,lst in tree.items():
        for idx,age in enumerate(lst):
            if age % 5 == 0:
                r,c = k
                for dir in range(8):
                    nr,nc = dy[dir]+r,dx[dir]+c
                    if 0 <= nr < N and 0 <= nc < N:
                        n = (nr,nc)
                        temp[n] += 1
    for k,cnt in temp.items():
        for c in range(cnt):
            tree[k].appendleft(1)
    # print('가을')
    # for row in martix:
    #     print(*row)
    # 겨울
    for i in range(N):
        for j in range(N):
            matrix[i][j] += A[i][j]
    # print('겨울')
    # for row in martix:
    #     print(*row)
    time += 1
    # print(time,'년')
    # print('-----------')
for lst in tree.values():
    answer += len(lst)

print(answer)