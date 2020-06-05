# 수 이어가기 # 21:45
n = int(input())
number = []  #갯수 저장용 리스트

num_list = [[n] for idx in range(n)] # 1~100까지의 경우의 수

for j in range(0,n):  # num_list[0]~num_list[n-1]
    num_list[j].append(j+1)
    count = 2 #이미 있는 두개 포함
    i = 2
    while 1:
        num_temp = num_list[j][i-2]-num_list[j][i-1]
        if num_temp < 0:
            break
        num_list[j].append(num_temp)
        count += 1
        i+=1
    number.append(count)

posi = number.index(max(number))
print(max(number))
print(*num_list[posi]) 
#22:37