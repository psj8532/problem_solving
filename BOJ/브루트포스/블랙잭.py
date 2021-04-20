#16:21
#뽑아야하는 카드의 수가 3장이므로
#3중for문을 이용하여 카드를 한장씩 골라내고 합을 구한다음 m과의 차이를 구함
#차이와 최솟값을 비교하여 최솟값 저장

n,m=map(int,input().split())
card = list(map(int,input().split()))
min_val=987654321
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            temp = card[i]+card[j]+card[k]
            if temp <= m:
                diff = m-temp
                if diff < min_val:
                    min_val = diff #차이가 최소일 때 최솟값을 최신화하지 않아서 틀렸음
                    result=temp
print(result)
#16:47