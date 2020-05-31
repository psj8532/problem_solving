# 색종이    #16:59
matrix = [[0]*101 for _ in range(101)]

n = int(input())

for num in range(1,n+1):
    data = list(map(int,input().split()))

    for y in range(data[1],data[1]+data[3]):
        for x in range(data[0],data[0]+data[2]):
            matrix[y][x] = num

for num in range(1,n+1):
    count = 0
    for y in range(101):
        for x in range(101):
            if matrix[y][x] == num:
                count+=1
    print(count)
#17:20