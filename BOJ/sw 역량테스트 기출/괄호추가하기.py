def subset(here):
    for next in range(here+2,n):
        a.append(next)
        temp = a[:]
        s.append(temp)
        subset(next)
        a.pop()


def operator(y,opcode,x):
    if opcode == '+':
        return y + x
    elif opcode == '-':
        return y-x
    else:
        return y*x


N = int(input())
matrix = list(input())
s = []
for i in range(0,N,2):
    matrix[i] = int(matrix[i])

n = N//2
for i in range(1,n):
    a = [i]
    temp = a[:]
    s.append(temp)
    subset(i)

max = matrix[0]
for i in range(0,N-1,2):
    max = operator(max, matrix[i+1], matrix[i+2])

for i in range(len(s)):
    sum = matrix[0]
    visited = [False]*N
    isPass = False
    for j in range(len(s[i])):
        visited[2*s[i][j]] = True
    for j in range(0, N-1, 2):
        if isPass:
            isPass = False
            continue
        if visited[j+2]:
            result = operator(matrix[j+2], matrix[j+3], matrix[j+4])
            sum = operator(sum, matrix[j+1], result)
            isPass = True
        else:
            sum = operator(sum, matrix[j+1], matrix[j+2])
            isPass = False
    if sum > max:
        max = sum

print(max)