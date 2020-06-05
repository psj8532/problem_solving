def solve(start, sum):
    global max
    for i in range(start,N,1):
        if i+matrix[i][0]<=N:
            solve(i+matrix[i][0], sum+matrix[i][1])
    if sum>max:
        max = sum

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
max = 0
solve(0, 0)
print(max)