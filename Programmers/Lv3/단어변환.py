# 19:27 ~ 19:59
def solution(begin, target, words):
    def dfs(k,word,goal):
        nonlocal answer
        if k == N:
            return
        if word == goal:
            answer = min(answer,k)
            return
        for i in range(N):
            if visited[i]: continue
            diff = 0
            for j in range(len(word)):
                if word[j] != words[i][j]:
                    diff += 1
                    if diff == 2: break
            if diff == 1:
                visited[i] = 1
                # print(word, ' => ', words[i])
                dfs(k+1,words[i],goal)
                visited[i] = 0

    answer = 9876543210
    N = len(words)
    visited = [0] * N
    dfs(0,begin,target)
    if answer == 9876543210: return 0

    return answer

ex1 = ("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])  # 4
ex2 = ("hit","cog",["hot", "dot", "dog", "lot", "log"]) # 0
print(solution(*ex2))