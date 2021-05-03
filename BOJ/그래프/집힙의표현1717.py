def find_set(x):
    if parent[x] == x: return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]

def union(y, x):
    py, px = find_set(y), find_set(x)
    if py > px:
        parent[px] = py
    elif py < px:
        parent[py] = px
    return

N, M = map(int,input().split())
parent = list(range(N + 1))
rank = [0] * (N + 1)
for _ in range(M):
    command, num1, num2 = map(int,input().split())
    if command:
        print('YES') if parent[num1] == parent[num2] else print('NO')
    else:
        union(num1, num2)