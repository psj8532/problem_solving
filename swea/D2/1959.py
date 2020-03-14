#두 개의 숫자열 # 6:12
import sys
sys.stdin = open("1959.text","r")

t=int(input())

for test_case in range(1,t+1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #짧은 숫자열과 긴 숫자열의 길이를 맞춰줌
    if len(a)>len(b):
        l = len(a)-len(b)
        long_str = 1
        for idx in range(l):
            b.append(0) #복붙시 조심
    elif len(a)<len(b):
        l = len(b)-len(a)
        long_str = 2
        for idx in range(l):
            a.append(0)
    
    result_list = []
    #숫자열 쉬프트
    for i in range(l+1):
            #곱하기
        result = 0
        for i in range(len(a)):
            mul = a[i]*b[i]
            result += mul
        result_list.append(result)
        
        if long_str == 1: #a열이 더 길면
            temp = b[len(b)-1]
            for j in range(len(b)-2,-1,-1):                            
                b[j+1]=b[j]
            b[0]=temp
        elif long_str == 2: #b열이 더 길면
            temp = a[len(b)-1]
            for j in range(len(a)-2,-1,-1):
                a[j+1]
                a[j+1]=a[j] # 복붙시 조심
            a[0]=temp
    max_val = max(result_list)
    print(f'#{test_case} {max_val}')

    # 7:15 종료