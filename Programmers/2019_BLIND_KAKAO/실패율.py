def solution(N, stages):
    answer = []
    fail = [0] * (N+1)
    total = [0] * (N+1)
    rate = [[0,i] for i in range(N+1)]
    for i in range(len(stages)):
        if stages[i] <= N:
            fail[stages[i]] += 1
        for j in range(1,stages[i]+1):
            if j > N: break
            total[j] += 1
    for i in range(1, N+1):
        rate[i][0] = fail[i] / total[i]
    rate.pop(0)

    rate.sort(reverse=True, key=lambda x:x[0])
    print(rate)
    for i in range(len(rate)):
        answer.append(rate[i][1])
    return answer


ex1 = [5, [2, 1, 2, 6, 2, 4, 3, 3]]
print(solution(*ex1))