# 10:52 ~ 11:06
# bfs 이용
# 뎁스를 인덱스로 갖는 리스트, 값은 갯수로
# from _collections import deque
#
# def solution(n, edge):
#     def bfs(start, depth):
#         deq = deque()
#         visited = [0] * (n+1)
#         deq.append([start, depth])
#         visited[start] = 1
#
#         while deq:
#             here, depth = deq.popleft()
#             for next in adj[here]:
#                 if not visited[next]:
#                     visited[next] = 1
#                     deq.append([next, depth+1])
#                     ds[depth+1] += 1
#
#         return depth
#
#
#     answer = 0
#     adj = {i:[] for i in range(1, n+1)}
#     ds = [0] * 50001
#     for s, e in edge:
#         adj[s].append(e)
#         adj[e].append(s)
#
#     d = bfs(1,0)
#     return ds[d]
#
# # n	vertex	return
# ex1 = (6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])	# 3
# print(solution(*ex1))

# 17:45 ~ 18:11
from _collections import deque

def solution(n, edge):
    answer = [0] * 20000
    def bfs(s, d):
        deq = deque([[s,d]])
        visited = [False] * (n + 1)
        visited[s] = True

        while deq:
            here, curr_depth = deq.popleft()
            answer[curr_depth] += 1
            for next in adj[here]:
                if not visited[next]:
                    deq.append([next, curr_depth + 1])
                    visited[next] = True
        return curr_depth

    adj = {i: [] for i in range(n+1)}
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
    rear = bfs(1, 0)
    return answer[rear]

print(solution(*(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])))