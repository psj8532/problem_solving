# 13:03 ~ 13:18
# 플로이드 워샬
# 1번 마을도 배달할 수 있고, 두 마을 사이의 경로가 두개 이상 있을 수도 있다는 것에 유의
def solution(N, road, K):
    answer, INF = 1, float('inf')
    adj = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        adj[i][i] = 0
    for s,e,c in road:
        if c < adj[s][e]: adj[s][e] = c
        if c < adj[e][s]: adj[e][s] = c

    for m in range(2,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                cost = adj[i][m] + adj[m][j]
                if adj[i][j] > cost: adj[i][j] = cost
    for j in range(2, N+1):
        if adj[1][j] <= K: answer += 1
    return answer

# N	road	K	result
ex1 = (5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],	3)	# 4
ex2 = (6,	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],	4)	# 4
print(solution(*ex2))