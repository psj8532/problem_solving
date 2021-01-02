# 24분
def solution(n):
    ans = 1
    here = n
    while here != 1:
        while not here % 2:
            here //= 2
        if here != 1:
            ans += 1
            here -= 1

    return ans

ex1 = 5 #2
ex2 = 6	#2
ex3 = 5000	#5
ex4 = 1000000000
ex5 = 14
print(solution(ex3))