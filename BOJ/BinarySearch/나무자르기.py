# 이분 탐색
# mid를 이용해서 해당 높이를 기준으로 나무를 잘랐을 때, 얼마나 잘라갈 수 있는지 파악
# 자르는 나무의 높이가 M보다 작다면 right를 mid-1로 설정
# 크거나 같다면 left를 mid로 설정

N, M = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()
left, right = 0, trees[-1]
answer = 0
while left <= right:
    mid = (left + right) // 2
    gain = 0
    for height in trees:
        val = height - mid
        if val > 0: gain += val
    if gain < M:
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1
print(answer)


# 13 15 15 15 17