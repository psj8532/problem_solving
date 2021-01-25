def solution(n, s, a, b, fares):
    INF = float('inf')
    dist = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dist[i][i] = 0
    for u,w,c in fares:
        dist[u][w] = c
        dist[w][u] = c

    answer = INF
    for m in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                val = dist[i][m] + dist[m][j]
                if val < dist[i][j]:
                    dist[i][j] = val

    answer = min(answer, dist[s][a]+dist[s][b])
    for m in range(1,n+1):
        val = dist[s][m] + dist[m][a] + dist[m][b]
        if val < answer:
            answer = val

    return answer


# n	s	a	b	fares	result
ex1 = (6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])	# 82
ex2 = (7,	3,	4,	1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])	# 14
ex3 = (6,	4,	5,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])	#18
print(solution(*ex3))