#17:20 #14889
import sys
sys.stdin=open("스타트와링크.text","r")
#n:총 인원수, n//2:팀원 수
#matrix에 정보 받음
#순열을 이용하여 팀을 조합(오름차순)
    #a의 길이는 n//2
    #in_perm의 길이는
#조합된 팀을 받아와서 결과 값 계산(완료하면 다음 조합 찾으러감)
    #조합된 팀을 받아오면, 조합된 리스트에 없는 숫자를 저장하는 리스트 만듬(상대팀)
    #능력치 계산
        #이중 for문 이용하여 자기 이외수 수와의 능력치 계산 , 위치 변경

def perm(a,k):
    if k==num:
        temp = a[:]
        data.append(temp)
    else:
        in_perm = [False]*n

        for i in range(k):
            in_perm[a[i]] = True
        for i in range(n-1,-1,-1):
            if in_perm[i]:
                posi = i
                break
        else:
            posi=0
        c=[0]*n
        cnt=0
        for i in range(posi,n):
            if in_perm[i]==False:
                c[cnt]=i
                cnt+=1
        for i in range(cnt):
            a[k]=c[i]
            perm(a,k+1)

n=int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
num = n//2
data=[]
a=[0]*num
perm(a,0)

min_val=987654321
for y in range(len(data)):
    val_1 = 0
    val_2 = 0
    data_away=[0]*num
    rear=-1
    for idx in range(n):
        if idx not in data[y]:
            rear+=1
            data_away[rear] = idx
    #우리팀
    for i in range(n-1):
        for j in range(i+1,len(data[y])):
            temp_y = data[y][i]
            temp_x = data[y][j]
            val_1 += matrix[temp_y][temp_x]
            val_1 += matrix[temp_x][temp_y]
    #상대팀
    for i in range(n-1):
        for j in range(i+1,len(data[y])):
            temp_y = data_away[i]
            temp_x = data_away[j]
            val_2 += matrix[temp_y][temp_x]
            val_2 += matrix[temp_x][temp_y]
    if val_1>=val_2:
        diff = val_1-val_2
    else:
        diff = val_2-val_1
    # diff = abs(val_2-val_1)
    if min_val>diff:
        min_val = diff

print(min_val)
#19:53