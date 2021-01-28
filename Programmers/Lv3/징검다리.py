# 11:16 ~ 12:16 # 효율성 실패
def solution(stones, k):
    stones += [float('inf')]
    answer, N = 0, len(stones)
    lst = stones[:]
    for i in range(N-k):
        lst[i+k] = min(stones[i+k], max(lst[i:i+k]))
    return lst[N-1]

# stones	k	result
ex1 = ([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3)	# 3
print(solution(*ex1))