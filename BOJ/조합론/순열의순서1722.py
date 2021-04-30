import math

N = int(input())
info = list(map(int,input().split()))
problem = info[0]
numbers = range(1, N+1)
answer = []
visit = [False] * N
if problem == 1:
    k = info[1]
    dividend, divisor = k - 1, N - 1
    while divisor:
        f = math.factorial(divisor)
        quotient = dividend // f
        reaminder = dividend % f
        cnt = idx = -1
        while cnt < quotient:
            idx += 1
            if not visit[idx]: cnt += 1
        answer.append(numbers[idx])
        visit[idx] = True
        dividend = reaminder
        divisor -= 1
    for i in range(N):
        if not visit[i]: answer.append(numbers[i])
else:
    sequence = info[1:]
    val = 0
    for i in range(N-1):
        num = sequence[i]
        cnt = idx = new_num = -1
        while new_num < num:
            idx += 1
            if not visit[idx]:
                cnt += 1
                new_num = numbers[idx]
        visit[idx]= True
        val += (math.factorial(N-1-i) * cnt)
    answer = [val + 1]
print(*answer)