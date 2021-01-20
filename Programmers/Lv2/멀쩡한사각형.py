#11:24 ~
def solution(w,h):
    answer = 1
    def gcd(y,x):
        a,b = max(y,x),min(y,x)
        r = a % b
        if r:
            return gcd(b,r)
        else:
            return b
    br_cnt = w + h - gcd(w,h)
    answer = w * h - br_cnt
    return answer

ex1 = [8,12] # 80
ex2 = [1,1] # 0
ex3 = [2,7] # 6
ex4 = [100000000,10000000]
print(solution(*ex3))
