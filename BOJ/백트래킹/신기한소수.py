import math

def check_prime(n):
    if n == 0 or n == 1: return False
    for j in range(2, math.floor(n**0.5) + 1):
        if not (n % j): return False
    return True

def dfs(number, k, answer):
    if k == N:
        answer.append(int(number))
        return answer
    for i in range(1, 10):
        num = number + str(i)
        if check_prime(int(num)): answer = dfs(num, k + 1, answer)
    return answer

N = int(input())
answer = dfs('', 0 , [])
for ans in answer:
    print(ans)