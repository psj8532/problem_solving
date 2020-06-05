#6603
#입력이 0 하나 나올때까지 while문으로 입력받기
# data[0]: 집합의 원소가 몇개인지
# data[1]~:집합안에 들어있는 숫자
# 순열 이용
# in_perm 대신 집합안에 있는 수를 이용
# in_perm true 만들때 a[i]가 들어있는 인덱스 찾고 거기를 true로 변환
def perm(a,k):
    if k==6:
        print(*a)
    else:
        in_perm = [False]*n
        for i in range(k):
            in_perm[s.index(a[i])] = True
        for i in range(n-1,-1,-1):
            if in_perm[i]:
                posi = i
                break
        else:
            posi=0
        cnt=0
        c=[0]*n
        for i in range(posi,n):
            if in_perm[i] == False:
                c[cnt] = s[i]
                cnt+=1

        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1)
tc=0
data=[]
while 1:
    data.append(list(map(int,input().split())))
    if len(data[tc])==1 and not data[tc][0]:
        break
    tc+=1

for t in range(tc):
    n = data[t][0]
    a=[0]*6
    s=[]
    for idx in range(1,1+n):
        s.append(data[t][idx])
    perm(a,0)
    print()