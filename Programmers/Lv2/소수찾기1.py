from itertools import permutations
import math

def solution(numbers):
    answer = 0
    primes = {}
    def checkPrime(num):
        if num <= 1: return False
        for i in range(2, math.floor(num**0.5) + 1):
            if not (num % i): return False
        return True

    for permSize in range(1, len(numbers)+1):
        perm = list(map(list,permutations(numbers, permSize)))
        for num in perm:
            num = int(''.join(num))
            if checkPrime(num) and num not in primes:
                primes[num] = True
                answer += 1

    return answer

print(solution("17"))