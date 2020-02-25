import sys
sys.stdin = open("N과M_2.text","r")

def perm(a,k,N):
    if k==m:
        if a[k-1]:
            print(*a)
    else:
        in_perm=[False]*(N+1)
        c=[0]*N
        start=1
        for i in range(k):
            in_perm[a[i]]=True
        for i in range(N,0,-1):
            if in_perm[i]:
                start = i
                break
        else:
            start = 0
        cnt=0
        for i in range(start+1,N+1):
            c[cnt]=i
            cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1,N)

n,m=map(int,input().split())
a=[0]*m
perm(a,0,n)