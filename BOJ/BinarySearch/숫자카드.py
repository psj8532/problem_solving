# 17:24 ~ 17:41
N = int(input())
cards = list(map(int,input().split()))
M = int(input())
check = list(map(int,input().split()))
answer = [0] * M
cards = sorted(cards)
for i, num in enumerate(check):
    left, right = 0, N-1
    while left <= right:
        mid = (left + right) // 2
        if num == cards[mid]:
            answer[i] = 1
            break
        elif num > cards[mid]: left = mid + 1
        else: right = mid - 1
print(*answer)