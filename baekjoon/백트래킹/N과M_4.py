
import sys
sys.stdin = open("N과M_3.text","r")

def perm(a,k,N):
    if k==m:
        print(*a)
    else:
        in_perm=[False]*(n+1)

        for i in range(k):
            in_perm[a[i]-1]=True
        for i in range(n,-1,-1):
            if in_perm[i]:
                start = i
                break
        else:
            start=0
        c=[0]*N
        cnt=0
        for i in range(start+1,n+1):
            if in_perm[i] == False:
                c[cnt]=i
                cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1,N)

n,m = map(int,input().split())
a=[0]*m
perm(a,0,n)
#18:41