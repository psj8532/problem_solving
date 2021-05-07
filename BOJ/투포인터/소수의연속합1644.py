def make_prime():
    check_primes = [0] * (N + 1)
    primes = []
    for i in range(2, N + 1):
        if check_primes[i]: continue
        primes.append(i)
        last = N // i
        j = 2
        while j <= last:
            nj = i * j
            check_primes[nj] = 1
            j += 1
    return primes

def two_pointer(primes):
    prime_size = len(primes)
    answer = sum_val = 0
    left = right = 0
    while left < prime_size and right < prime_size:
        sum_val += primes[right]
        while sum_val >= N:
            if sum_val == N: answer += 1
            sum_val -= primes[left]
            left += 1
        right += 1
    return answer

N = int(input())
print(two_pointer(make_prime()))
