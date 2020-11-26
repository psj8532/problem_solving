import copy


D = [(-1,0),(1,0),(0,-1),(0,1)]
N,M,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
smells = dict() # 냄새 저장
shark_fd = list(map(int,input().split()))
shark_d = {i: [] for i in range(1,N+1)}
for i in range(1,M+1):
    sd = {j: '' for j in range(4)}
    for j in range(0,4):
        t = list(map(int,input().split()))
        for idx, val in enumerate(t):
            t[idx] -= 1
        sd[j] = t
    shark_d[i] = sd

# 상어가 있는 좌표 받아옴
cur = dict()
for i in range(N):
    for j in range(N):
        smells[(i, j)] = [0,0]
        if matrix[i][j]:
            smells[(i, j)] = [matrix[i][j],K]
            cur[(i,j)] = [matrix[i][j],shark_fd[matrix[i][j]-1]-1] # 상어가 여러마리일 떄, 잠깐 저장하기 위해 리스트로 만듬 # 번호, 방향
# 1번 상어만 남았는지 체크 or 1000초가 지났는지 확인
t = 0
while t < 1000:
    t += 1
    # 현재 존재하는 모든 상어 순회
    tcur = dict()
    for here,lst in cur.items():
        y,x = here
        idx,d = lst[0],lst[1]
        non_smell = []
        smell = []
        # 상어의 현재 방향을 기준으로 우선 순위대로 방향 확인, 냄새 없는 곳은 따로 넣기
        for dir in shark_d[idx][d]:
            ny,nx = y+D[dir][0],x+D[dir][1]
            if 0 <= ny < N and 0 <= nx < N and not smells[(ny,nx)][1]:
                non_smell.append((ny,nx,dir))
            elif 0 <= ny < N and 0 <= nx < N and smells[(ny,nx)][1] and smells[(ny,nx)][0] == idx:
                smell.append((ny,nx,dir))
        if non_smell:
            ny,nx,nd = non_smell[0]
            if (ny, nx) in tcur and tcur[(ny, nx)][0] != 0:
                old_idx = tcur[(ny,nx)][0]
                # 번호가 높은 상어는 어차피 나중에 밀리므로 지금 후보에 넣지 않음
                if idx < old_idx:
                    tcur[(ny,nx)] = [idx,nd]
            else:
                tcur[(ny, nx)] = [idx, nd]
        elif smell:
            ny,nx,nd = smell[0]
            # 어차피 냄새가 있으면 다른 상어는 못옴
            tcur[(ny, nx)] = [idx, nd]

    # 이동하기 전에 있던 좌표에 있는 냄새 -1
    for k in smells.keys():
        if smells[k][1] > 1:
            smells[k][1] -= 1
            smells[k] = [smells[k][0],smells[k][1]]
        else:
            smells[k] = [0,0]
    for k in tcur.keys():
        smells[k] = [tcur[k][0],K]
    cur = copy.deepcopy(tcur)
    isEnd = True
    for k in cur.keys():
        if cur[k][0] != 1:
            isEnd = False
    if isEnd: break

if isEnd:
    print(t)
else:
    print(-1)
