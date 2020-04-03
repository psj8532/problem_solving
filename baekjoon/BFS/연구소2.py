import sys
sys.stdin=open("연구소2.txt","r")
from _collections import deque

def bfs():
    global depth_min
    while deq:
        here=deq.popleft()
        y,x = here[0],here[1]
        for dir in range(len(direct)):
            new_y,new_x=y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<n and 0<=new_x<n and Matrix[new_y][new_x]!=1 and Visited[new_y][new_x]==-1:
                deq.append((new_y,new_x))
                Visited[new_y][new_x]=Visited[y][x]+1
def perm(a,k):
    if k==m:
        temp=a[:]
        S.append(temp)
    else:
        in_perm=[False]*len(Virus)
        for i in range(k):
            in_perm[a[i]]=True
        for i in range(len(Virus)-1,-1,-1):
            if in_perm[i]:
                posi=i+1
                break
        else:
            posi=0
        c=[0]*len(Virus)
        cnt=0
        for i in range(posi,len(Virus)):
            if not in_perm[i]:
                c[cnt]=i
                cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1)

direct=[(-1,0),(0,1),(1,0),(0,-1)]
n,m=map(int,input().split())
Virus=[]
Matrix=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if Matrix[i][j]==2:
            Virus.append((i,j))

S=[]
a=[0]*m
perm(a,0)
depth_min=9876543210
for i in range(len(S)):
    deq=deque()
    isFail=False
    result=0
    Visited = [[-1] * n for _ in range(n)]
    for j in range(m):
        deq.append((Virus[S[i][j]][0],Virus[S[i][j]][1]))
        Visited[Virus[S[i][j]][0]][Virus[S[i][j]][1]]=0
    bfs()
    for r in range(n):
        for c in range(n):
            if Visited[r][c]==-1 and Matrix[r][c]!=1:
                isFail=True
                result=-1
                break
            elif Visited[r][c]>=0:
                if Visited[r][c]>result:
                    result=Visited[r][c]
        if isFail:
            break
    if not isFail and depth_min>result:
        depth_min=result
if depth_min==9876543210:
    print(-1)
else:
    print(depth_min)