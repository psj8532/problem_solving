N, S = map(int,input().split())
numbers = list(map(int,input().split()))
INF = float('inf')
answer, left, right = INF, 0, 0
accm = 0

while left < N:
    curr = accm + numbers[right]
    if curr >= S:
        cnt = right - left + 1
        if cnt < answer: answer = cnt
        accm -= numbers[left]
        left += 1
    elif right == N-1: break
    else:
        accm = curr
        right += 1

if answer == INF: print(0)
else: print(answer)