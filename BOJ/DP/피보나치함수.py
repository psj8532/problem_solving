#1003
def fibo(n):
    if M[n] != [0,0]:
        return M[n]
    else:
        if n == 0:
            M[n][0],M[n][1] = 1, 0
        elif n == 1:
            M[n-1][0], M[n-1][1] = 1, 0
            M[n][0], M[n][1] = 0, 1
        else:
            M1 = fibo(n-1)
            M[n-1][0], M[n-1][1] = M1[0], M1[1]
            M[n][0], M[n][1] = M[n-1][0]+M[n-2][0], M[n-1][1]+M[n-2][1]
        return M[n]


t = int(input())
M = [[0,0] for i in range(41)]
for tc in range(t):
    N = int(input())
    answer = fibo(N)
    print(*answer)