# 11:16 ~ 12:16
def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        m = (left + right) // 2
        cnt = 0
        for v in stones:
            if v < m:
                cnt += 1
                if cnt >= k:
                    right = m - 1
                    break
            else:
                cnt = 0
        else:
            answer = m
            left = m + 1
    return answer

# stones	k	result
ex1 = ([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3)	# 3
print(solution(*ex1))