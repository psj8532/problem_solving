import sys
sys.stdin = open("사다리조작.txt","r")

def check():
    for c in range(0,2*N-1,2):
        visited = [[0] * (2 * N - 1) for _ in range(H + 2)]
        flag = True
        y,x = 0,c
        while y != H+1 and flag:
            flag = False
            for dir in range(3):
                ny,nx = y+direct[dir][0],x+direct[dir][1]
                if 0<=nx<2*N-1 and matrix[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    y,x = ny,nx
                    flag = True
                    break
        if y == H+1:
            if x != c:
                return False
        elif y!=H+1 and not flag:
            return False
    return True

def comb(k,cnt,length,a,s):
    if k == cnt:
        temp = a[:]
        s.append(temp)
        return
    else:
        in_perm=[False]*length
        for i in range(k):
            in_perm[a[i]] = True
        for i in range(length-1, -1, -1):
            if in_perm[i]:
                posi = i+1
                break
        else:
            posi = 0
        count = 0
        c=[0]*length
        for i in range(posi, length):
            if not in_perm[i]:
                c[count] = i
                count += 1
        for i in range(count):
            a[k] = c[i]
            comb(k+1,cnt,length,a,s)


def solve(cnt):
    global isEnd
    if cnt>3:
        return False
    s = []
    a = [0]*cnt
    comb(0,cnt,len(candidate),a,s)
    for i in range(len(s)):
        for j in range(cnt):
            idx = s[i][j]
            y,x = candidate[idx][0],candidate[idx][1]
            matrix[y][x] = 1
        if check(): #참이면 조합의 갯수 반환하며 함수 종료
            return cnt #재귀이므로 바로 종료할 수 있도록 설
        for j in range(cnt):
            idx = s[i][j]
            y,x = candidate[idx][0],candidate[idx][1]
            matrix[y][x] = 0
    cnt = solve(cnt+1)
    return cnt

direct = [(0,1),(0,-1),(1,0)]
N,M,H = map(int,input().split())
matrix = [[0]*(2*N-1) for _ in range(H+2)]
candidate = []
if M:
    data = [list(map(int,input().split())) for _ in range(M)]
    for i in range(M):
        matrix[data[i][0]][2*(data[i][1]-1)+1] = 1
for j in range(0, 2*N, 2):
    for i in range(H+2):
        matrix[i][j] = 1
for i in range(1,H+1):
    for j in range(1,2*N-1,2):
        if not matrix[i][j]:
            candidate.append((i,j))
#check
if check():
    print(0)
else:
    #추가하는 사다리의 갯수 (재귀)
    cnt = solve(1)
    if cnt:
        print(cnt)
    else:
        print(-1)