# 쉬운 거스름돈 # 16:07
t=int(input())

type=[50000,10000,5000,1000,500,100,50,10]

for test_case in range(1,t+1):
    won = int(input())
    num = []
    for i in range(len(type)):
        num.append(won//type[i])
        if won//type[i]:
            won= won-type[i]*num[i]
    print(f'#{test_case}')
    print(*num)
# 16:19