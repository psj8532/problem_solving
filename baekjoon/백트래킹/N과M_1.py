def perm(a,k,N):
    if k==m:
        print(*a)
    else:
        in_perm=[False]*(N+1)
        c=[0]*N

        for i in range(k):
            in_perm[a[i]]=True
        cnt=0
        for i in range(1,N+1):
            if in_perm[i]==False:
                c[cnt]=i
                cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1,N)

n,m=map(int,input().split())
a=[0]*m
perm(a,0,n)