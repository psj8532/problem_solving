# 12:54 ~ 14:11
def solution(tickets):
    def dfs(h,k,v):
        if k == N:
            return True
        for i in range(N):
            if tickets[i][0] == h and not v[i]:
                v[i] = 1
                answer.append(tickets[i][1])
                if dfs(tickets[i][1],k+1,v): return True
                answer.pop()
                v[i] = 0
        return False

    tickets.sort()
    N = len(tickets)
    visited = [0]*N
    answer = ['ICN']
    dfs('ICN', 0, visited)
    return answer

ex1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]  # ["ICN", "JFK", "HND", "IAD"]
ex2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
ex3 = [["ICN","ICN"],["ICN","ICN"],["ICN","ICN"]]
print(solution(ex2))