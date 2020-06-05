# 수열 # 13:20
n=int(input()) #수열의 길이
num_str = list(map(int,input().split()))
count = 1
count_list = [[] for _ in range(2)] #큰거 판단, 작은거 판단용으로 2차원 리스트 생성
result_list = [] # 큰 거 판별 리스트에서 하나랑 작은거 판별 리스트에서 하나 뽑아와서 저장


#앞에서부터 왼쪽이 큰지 확인
for i in range(n-1):
    #[0]이 [1]보다 큰지 확인
    if num_str[i]>=num_str[i+1]:
        count+=1        
    else:
        count_list[0].append(count)#현재까지 찾은 길이 저장
        count = 1 #카운트1로 설정 후 현재부터 재시작 #다음 인덱스부터 시작하므로 1로 초기화
count_list[0].append(count)#마지막까지 적용됬을 때의 길이를 반영하기 위해
count = 1
result_list.append(max(count_list[0])) #연속된 숫자 중 가장 긴 길이를 저장 리스트

#앞에서부터 뒤가 큰지 확인
for i in range(n-1):
    if num_str[i]<=num_str[i+1]:
        count+=1
    else:
        count_list[1].append(count)
        count = 1
count_list[1].append(count)

result_list.append(max(count_list[1]))

result = max(result_list) #가장 긴 길이 저장

print(result)
# 2:12 완료