# 12:03 ~ 12:32
def solution(arr):
    def find_prime(end):
        end = int(end**(1/2))+1
        for i in range(2,end):
            if not primes[i]:
                for j in range(i+i, len(primes), i):
                    primes[j] = 1
        for i in range(2,len(primes)):
            if not primes[i]:
                prime.append(i)
    answer = 1
    max_arr = max(arr)
    primes = [0] * (max_arr+1)
    prime = []
    find_prime(max_arr+1)

    dict = {}
    for num in arr:
        val = num
        for p in prime:
            if p not in dict:
                dict[p] = []
            exp = 0
            while val > 1 and not (val % p):
                exp += 1
                val //= p
            if exp: dict[p].append(exp)

    for k,v in dict.items():
        if v:
            answer *= (k**(max(v)))

    return answer

# arr	result
ex1 = [2,6,8,14]	# 168
ex2 = [1,2,3]	# 6
print(solution(ex2))