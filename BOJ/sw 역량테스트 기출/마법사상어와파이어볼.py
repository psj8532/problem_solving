def divide(tlst):
    nm = ns = 0
    isCheck = [0,0]
    for lst in tlst:
        y, x, m, s, d = lst
        nm += m
        ns += s
        isCheck[d % 2] = 1
    nm //= 5
    ns //= len(tlst)
    if isCheck == [1,1]:
        dlst = [1, 3, 5, 7]
    else:
        dlst = [0, 2, 4, 6]
    if nm != 0:
        for i in range(4):
            before.append([y,x,nm,ns,dlst[i]])


def move(tlst):
    y, x, m, s, d = tlst
    ny,nx = y,x
    if d == 0:
        ns = s
        if s >= N:
            ns %= N
        ny = y - ns
        if ny < 0:
            ny = N - abs(ny)
    elif d == 1:
        ns = s
        if s >= N:
            ns %= N
        ny = y - ns
        if ny < 0:
            ny = N - abs(ny)
        nx = (x + s) % N
    elif d == 2:
        nx = (x + s) % N
    elif d == 3:
        ny = (y + s) % N
        nx = (x + s) % N
    elif d == 4:
        ny = (y + s) % N
    elif d == 5:
        ns = s
        if s >= N:
            ns %= N
        nx = x - ns
        if nx < 0:
            nx = N - abs(nx)
        ny = (y + s) % N
    elif d == 6:
        ns = s
        if s >= N:
            ns %= N
        nx = x - ns
        if nx < 0:
            nx = N - abs(nx)
    else:
        ns = s
        if s >= N:
            ns %= N
        ny = y - ns
        if ny < 0:
            ny = N - abs(ny)
        ns = s
        if s >= N:
            ns %= N
        nx = x - ns
        if nx < 0:
            nx = N - abs(nx)

    if (ny,nx) in visited:
        visited[(ny,nx)].append([ny,nx,m,s,d])
    else:
        visited[(ny,nx)] = [[ny,nx,m,s,d]]


N,M,K = map(int,input().split())
before = []
for _ in range(M):
    arr = list(map(int,input().split()))
    arr[0] -= 1
    arr[1] -= 1
    before.append(arr)
count = 0
while count < K:
    count += 1
    visited = dict()
    for lst in before:
        move(lst)
    before = []
    for p,plst in visited.items():
        if len(plst) > 1:
            divide(plst)
        else:
            before.append(plst[0])
answer = 0
for lst in before:
    answer += lst[2]
print(answer)