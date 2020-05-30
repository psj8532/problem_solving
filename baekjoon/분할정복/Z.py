import sys
sys.stdin = open("Z.txt", "r")
import time

stime = time.time()

def div(sy,ey,sx,ex,n):
    global cnt, flag
    if n == 2:
        for i in range(sy,ey):
            for j in range(sx,ex):
                if (i,j) == (r,c):
                    flag = True
                    return
                cnt += 1
        return
    mid = n>>1
    div(sy, sy + mid, sx, sx + mid, mid)
    if flag: return
    div(sy, sy + mid, sx + mid, ex, mid)
    if flag: return
    div(sy + mid, ey, sx, sx + mid, mid)
    if flag: return
    div(sy + mid, ey, sx + mid, ex, mid)


N,r,c = map(int,input().split())
s = 2**N
cnt = 0
flag = False
div(0,s,0,s,s)
print(cnt)
print('time: {}'.format(time.time()-stime))

# 값을 리스트로 만들었다가 메모리 초과 => 2^15 크기의 2차원 리스트를 만들어야하기 때문이다.
# 분할할 때 2로 나누려면 2**N을 가져와야하는데 N을 가져왔음