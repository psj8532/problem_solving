# 11:16 ~ 12:16 # 효율성 실패
def solution(stones, k):
    answer, N = 0, len(stones)
    stones += [float('inf')]
    lst = stones[:]
    for i in range(N-k+1):
        lst[i+k] = min(stones[i+k], max(lst[i:i+k]))
    return lst[N]

# def solution(stones, k):
#     def min(a, b):
#         if a < b: return a
#         else: return b
#
#     def max(s, e):
#         m = lst[s]
#         for j in range(s,e):
#             if lst[j] > m:
#                 m = lst[j]
#         return m
#
#     answer, N = 0, len(stones)
#     stones += [float('inf')]
#     lst = stones[:]
#     for i in range(N-k+1):
#         lst[i+k] = min(stones[i+k], max(i,i+k))
#     return lst[N]

# stones	k	result
ex1 = ([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3)	# 3
print(solution(*ex1))