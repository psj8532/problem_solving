def solution(m, k):
    answer = ''
    visited = [False] * len(m)
    idx = 0
    for key in k:
        for i in range(idx, len(m)):
            if key == m[i] and not visited[i]:
                visited[i] = True
                idx = idx+1
                break
    for i in range(len(m)):
        if not visited[i]:
            answer += m[i]
    return answer


ex1 = ["kkaxbycyz", "abc"]
ex2 = ["acbbcdc", "abc"]
print(solution(*ex1))