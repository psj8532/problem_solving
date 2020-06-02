import sys
sys.stdin = open("Z.txt", "r")
import time

stime = time.time()

def div(sy,sx,n):
    global cnt,flag
    if n == 2:
        for i in range(sy,sy+n):
            for j in range(sx,sx+n):
                if (i,j) == (r,c):
                    flag = True
                    return
                cnt += 1
    else:
        mid = n >> 1
        for i in range(2):
            for j in range(2):
                div(sy+mid*i, sx+mid*j, mid)
                if flag: return

N,r,c = map(int,input().split())
s = 2**N
cnt = 0
flag = False
div(0,0,s)
print(cnt)
print('time: {}'.format(time.time()-stime))

# 값을 리스트로 만들었다가 메모리 초과 => 2^15 크기의 2차원 리스트를 만들어야하기 때문이다.
# 분할할 때 2로 나누려면 2**N을 가져와야하는데 N을 가져왔음