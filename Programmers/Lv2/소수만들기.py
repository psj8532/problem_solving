from itertools import combinations

def solution(nums):
    answer = 0
    def prime_check(end):
        end = int(end**(1/2)) + 1
        for i in range(2, end):
            if not primes[i]:
                for j in range(i+i, len(primes), i):
                    primes[j] = 1

    max_val = max(nums) * 3
    primes = [0] * max_val
    prime_check(max_val)
    comb = list(map(list,combinations(nums,3)))
    for c in comb:
        total = 0
        for val in c:
            total += val
        if not primes[total]:
            answer += 1
    return answer

# nums	result
ex1 = [1,2,3,4] # 1
ex2 = [1,2,7,6,4]	# 4
print(solution(ex2))