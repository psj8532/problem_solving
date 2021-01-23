# 효율성 통과 못함
def solution(n, money):
    def recursion(total, idx):
        nonlocal answer
        if total == n:
            answer = (answer + 1) % 1000000007
            return
        if idx < 0: return
        for i in range(idx,-1,-1):
            unit = money[i]
            q = (n-total) // unit
            for j in range(q+1,0,-1):
                temp = unit * j
                if total + temp > n: continue
                recursion(total+temp, i-1)


    answer, N = 0, len(money)
    recursion(0, N-1)
    return answer

# n	money	result
ex1 = (5, [1,2,5])	# 4
ex2 = (100000, [i for i in range(1,101)])
ex3 = (7, [2,4,5])
print(solution(*ex3))