# 다솔이의 월급 상자    # 21:47
import sys
sys.stdin = open("6692.text","r")

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    result = 0
    for i in range(n):
        p, x = input().split()
        p = float(p)
        x = int(x)

        mul = p*x
        result += mul
    print('#{} {}'.format(test_case, result))

# 22:00