# 20:03 ~
def solution(n, weak, dist):
    def dfs(w_idx, d_idx, visited, cnt):
        nonlocal answer
        if d_idx == -1:
            answer = -1
            return
        elif visited[w_idx] and d_idx != D-1:

            if cnt < answer:
                answer = cnt
            return
        distance, start = dist[d_idx], weak[w_idx]
        end = (start + distance) % n
        idx = w_idx
        c = 0
        while weak[idx] <= end:
            idx = (idx+1) % W
            # print(idx)
            visited[idx] = 1
            c += 1
        # print()
        dfs(idx, d_idx-1, visited, cnt + c)
        idx -= 1
        while c > 0:
            visited[idx] = 0
            idx = (idx - 1) % W
            if idx == -1: idx = n - 1
            c -= 1


    answer, W, D = 9876543210, len(weak), len(dist)
    visited = [0] * W
    for i in range(W):
        visited[i] = 1
        dfs(i, D-1, visited, 0)
        visited[i] = 0
    return answer

# n	weak	dist	result
ex1 = (12,	[1, 5, 6, 10],	[1, 2, 3, 4])	# 2
ex2 = (12,	[1, 3, 4, 9, 10],	[3, 5, 7])	# 1
print(solution(*ex1))
# print(solution(*ex2))