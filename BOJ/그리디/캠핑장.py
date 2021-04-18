tc= 0
while True:
    tc += 1
    L, P, V = map(int,input().split())
    if (L, P, V) == (0, 0, 0): break
    q = V // P
    answer = q * L
    remainder = V % P
    if remainder <= L: answer += remainder
    else: answer += L
    print('Case {}: {}'.format(tc, answer))