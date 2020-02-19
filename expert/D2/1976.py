# 시각 덧셈 # 15:55
t=int(input())

for test_case in range(1,t+1):
    time = list(map(int,input().split()))
    #hour, minute
    minute = 0
    hour = 0
    hour = time[0]+time[2]
    minute = time[1]+time[3]
    if minute>59:
        minute-=60
        hour+=1
    if hour>12:
        hour-=12

    print(f'#{test_case} {hour} {minute}')

# 16:04

