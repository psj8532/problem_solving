#15:15
#(몸무게,키)
# for문으로 자기를 제외한 나머지를 탐색하면서 자기보다 큰 덩치가 몇명인지 카운트
# 카운트 한 수를 리스트에 추가하고 다음 사람기준으로 다시 탐색
n = int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
rank_list=[]
for i in range(n):
    cnt = 0
    for j in range(n):
        if i!=j and data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            cnt+=1
    rank_list.append(cnt+1)
print(*rank_list)
#15:30