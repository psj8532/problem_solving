from _collections import deque


def check_zero(deq,c):
    for v in deq:
        if not v:
            c += 1
    return c


N,K = input().split()
N,K = int(N), int(K)
arr = list(map(int,input().split()))
U,D = deque(arr[:N]),deque(arr[2*N-1:N-1:-1])
robot = deque([0]*N)
cnt = check_zero(U,0)
cnt = check_zero(D,cnt)
count = 0
while cnt < K:
    count += 1
    # 회전
    D.append(U.pop())
    U.appendleft(D.popleft())
    robot.rotate(1)
    robot[0] = 0
    # 이동
    robot[-1] = 0 # 로봇 내림
    for i in range(N-2,-1,-1):
        if robot[i] and not robot[i+1] and U[i+1]:
            U[i+1] -= 1
            robot[i+1] = 1
            robot[i] = 0
            # U[i] -= 1
    # 로봇 올림
    if U[0]:
        U[0] -= 1
        robot[0] = 1
    cnt = check_zero(U,0)
    cnt = check_zero(D,cnt)

print(count)