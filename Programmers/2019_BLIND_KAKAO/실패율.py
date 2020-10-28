def solution(N, stages):
    answer = []
    matrix = [[0]*2 for _ in range(N+2)]
    rate = [[0,i] for i in range(N+1)]
    for stage in stages:
        matrix[stage][0] += 1
    matrix[N+1][1] = matrix[N+1][0]
    for i in range(N,0,-1):
        matrix[i][1] = matrix[i+1][1] + matrix[i][0]
        if matrix[i][1] == 0:
            rate[i][0] = 0
        else:
            rate[i][0] = matrix[i][0] / matrix[i][1]

    rate.sort(reverse=True, key=lambda x:x[0])
    for i in range(len(rate)):
        if rate[i][1] == 0: continue
        answer.append(rate[i][1])
    return answer


ex1 = [5, [2, 1, 2, 6, 2, 4, 3, 3]]
ex2 = [4, [4,4,4,4]]
print(solution(*ex2))