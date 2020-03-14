# 간단한 압축 풀기 # 15:15
import sys
sys.stdin = open("1946.text","r")

t  = int(input())

for test_case in range(1, t+1):
    n = int(input())
    result=[[0]*10 for i in range(n)]
    data = []
    for k in range(n):
        ch, num = input().split()
        for i in range(int(num)):
            data.append(ch)
    print('#{}'.format(test_case))

    for i in range(len(data)):
        if i%10 == 0 and i != 0:
            print()
        print('{}'.format(data[i]),end='')
        
    print()

# 20:30





    # x = 0
    # IsEnd = False
    # for i in range(n): 
    #     for j in range(10):
    #         if x<len(data):            
    #             result[i][j] = data[x]
    #             print('{}'.format(result[i][j]), end='')
    #             x+=1
    #         else:
    #             IsEnd = True
    #     print()
    #     if IsEnd == True:
    #         break

    # for i in range(n):
    #     for j in range(10):
    #         if result[i][j]:
    #             print('{}'.format(result[i][j]), end='')
    #             if j==9:
    #                 print()
    #         else:
    #             continue