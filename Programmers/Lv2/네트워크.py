# 11:23 ~ 11:31
def solution(n, computers):
    def dfs(num):
        stack = []
        stack.append(num)

        while stack:
            here = stack.pop()
            if not visited[here]:
                visited[here] = 1
                for next in range(n - 1, -1, -1):
                    if next != num and not visited[next] and computers[here][next]:
                        stack.append(next)
        return

    answer = 0
    visited = [0] * n
    for num in range(n):
        if not visited[num]:
            dfs(num)
            answer += 1

    return answer