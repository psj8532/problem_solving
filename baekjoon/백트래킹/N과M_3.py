#17:45
import sys
sys.stdin=open("N과M_3.text","r")

def perm(a,k,N):
    if k==m:
        print(*a)
    else:
        for i in range(len(c)):
            a[k]=c[i]
            perm(a,k+1,N)

n, m = map(int,input().split())
a=[0]*m
c=list(range(1,n+1))
perm(a,0,n)
#18:09