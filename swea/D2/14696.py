# 딱지 놀이 # 10:35
import sys
sys.stdin = open("14696.text","r")

n = int(input())
for t in range(n):
    # data=[]
    matrix = [[0]*5 for _ in range(2)]
    for num in range(2):
        data = list(map(int,input().split()))

        for i in range(1, len(data)):
            if data[i] == 4:
                matrix[num][4]+=1
            elif data[i] == 3:
                matrix[num][3] += 1
            elif data[i] == 2:
                matrix[num][2] += 1
            elif data[i] == 1:
                matrix[num][1] += 1

    for x in range(4,0,-1):
        if matrix[0][x]>matrix[1][x]:
            print('A')
            break
        elif matrix[0][x]<matrix[1][x]:
            print('B')
            break
    else:
        print('D')

# 11:06
            