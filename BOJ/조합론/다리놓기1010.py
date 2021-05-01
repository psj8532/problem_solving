import math

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    print(math.factorial(M) // (math.factorial(M - N) * math.factorial(N)))