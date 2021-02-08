N = int(input())
ns = list(map(int,input().split()))
M = int(input())
ms = list(map(int,input().split()))
ns.sort()

def binary_search(l, r, v):
    if l >= r:
        if ns[r] == v: return 1
        else: return 0
    mid = (l + r) // 2
    if ns[mid] == v: return 1
    elif ns[mid] > v: return binary_search(l, mid, v)
    else: return binary_search(mid+1, r, v)

answer = []
for m in ms:
    ans = binary_search(0, N-1, m)
    answer.append(ans)
for row in answer:
    print(row)