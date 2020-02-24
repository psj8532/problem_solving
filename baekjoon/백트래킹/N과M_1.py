#19:00
import sys
sys.stdin=open("N과M_1.text","r")
# sys.setrecursionlimit(10**6)

def perm(a,k,N):
    if k==N:
        print(*a)
    else:
        in_perm=[False]*(N+1)
        c=[0]*(N+1)

        for i in range(k):
            in_perm[a[i]]=True
        cnt=0
        for i in range(1,N+1):
            if in_perm[i]==False:
                c[i]=i
                cnt+=1
        for i in range(1,cnt+1):
            a[k]=c[i] #cnt가 n의 갯수에 근접하게 많아서 인덱스 초과
            perm(a,k+1,N)

n,m=map(int,input().split())
a=[0]*m
perm(a,0,n)