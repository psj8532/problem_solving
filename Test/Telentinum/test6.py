from collections import deque

# def countPerms(n):
#     # Wr:ite your code here
#     answer = 0
#     adj = {
#         'a': ['e'],
#         'o': ['i', 'u'],
#         'e': ['a', 'i'],
#         'i': ['a','e','o','u'],
#         'u': ['a'],
#     }
#     deq = deque()
#     for k,v in enumerate(adj):
#         deq.append([v,1])
#     while deq:
#         h,d = deq.popleft()
#         if d == n:
#             answer += 1
#         else:
#             for next in adj[h]:
#                 if d + 1 <= n:
#                     deq.append([next,d+1])
#     return answer % (10**9+7)
#
# print(countPerms(2))
# bfs 로 풀었으나 n이 최대 10^12이므로 시간초과

def countPerms(n):
    # Write your code here
    answer = 0
    adj= [
        [1,2,4],
        [0,2],
        [1,3],
        [2],
        [2,3],
    ]
    dp = [1] * 5
    for i in range(1,n):
        arr = dp[:]
        for j in range(5):
            val = 0
            for idx in adj[j]:
                val += arr[idx]
            dp[j] = val
    answer = sum(dp)
    return answer % (10**9+7)

print(countPerms(3))
# dp로 접근
# dp 리스트에는 각 모음이 올 수 있는 경우의 수를 저장
# 현재 글자를 기준으로 이전 글자는 이미 정해져있으므로 이전 dp 리스트의 해당 모음 인덱스 합을 현재 dp 리스트로 최신화