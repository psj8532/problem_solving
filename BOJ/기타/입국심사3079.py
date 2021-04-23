N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
times = sorted(T)
left, right = times[0], times[-1] * M
answer = 0

while left <= right:
    people = 0
    mid = (left + right) // 2
    for t in times:
        if t > mid: break
        people += mid // t
    if people >= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)