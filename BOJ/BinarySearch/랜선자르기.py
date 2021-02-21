# 11:24~ 11:37
K, N = map(int,input().split())
wires = []
for _ in range(K):
    wire = int(input())
    wires.append(wire)
wires = sorted(wires)
left, right = 1, wires[-1]
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for wire in wires:
        cnt += wire // mid
    if cnt >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)