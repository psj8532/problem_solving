# 파리 퇴치 # 10 : 09
import sys
sys.stdin = open("2001.text","r")

t = int(input())

for test_case in range(1, t+1):
    matrix = []
    n, m = map(int,input().split())
    for i in range(n):
        matrix.append(list(map(int,input().split())))
        
    max_val = 0

    for y in range(n-m+1):
        for x in range(n-m+1):
            sum_val = 0
            for i in range(y, y + m):
                for j in range(x, x + m):
                    sum_val += matrix[i][j]
            if sum_val > max_val:
                max_val = sum_val
    
    print('#{} {}'.format(test_case, max_val))