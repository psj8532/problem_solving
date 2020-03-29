import sys
sys.stdin=open("치킨배달.txt","r")

def check():
    result_min=9876543210
    for idx in range(len(s)):
        cd=0
        isFail=False
        for i in range(n):
            for j in range(n):
                if matrix[i][j]==1:
                    d_min=9876543210
                    for c in s[idx]: #집에서 치킨집들과의 최소거리 구하기
                        y,x=chicken[c][0],chicken[c][1]
                        d=abs(y-i)+abs(x-j)
                        if d<d_min:
                            d_min=d
                    if cd+d_min>result_min:
                        isFail=True
                        break
                    else:
                        cd+=d_min
            if isFail:
                break
        else:
            result_min=cd
    return result_min

def perm(a,k):
    if k==m:
        temp=a[:]
        s.append(temp)
        a=[0]*m
    else:
        in_perm=[False]*len(chicken)

        for i in range(k):
            in_perm[a[i]]=True
        for i in range(len(chicken)-1,-1,-1):
            if in_perm[i]:
                posi=i
                break
        else:
            posi=-1
        c=[0]*len(chicken)
        cnt=0
        for i in range(posi+1,len(chicken)):
            if not in_perm[i]:
                c[cnt]=i
                cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1)

n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
a=[0]*m
chicken=[]
s=[]
for i in range(n):
    for j in range(n):
        if matrix[i][j]==2:
            chicken.append((i,j))
perm(a,0)

result=check()
print(result)