# 주사위 쌓기 # 17:06

# (a,f),(b,d),(c,e) 쌍
# a b c d e f 들어오는 순서
n = int(input())
dice_list=[] # n개의 주사위
for i in range(n): # n개의 주사위를 2차원 리스트에 저장
    dice = list(map(int,input().split()))
    # [0]=>[5], [1]=>[3], [2]=>[4]
    # [0]=>[3], [1]=>[4], [2]=>[5]
    dice[3],dice[4],dice[5] = dice[5],dice[3],dice[4]
    dice_list.append(dice)
sum_list=[]
#아랫면을 [0], 윗면을 [5]에 둠
for i in range(6): # 밑면에 올 수 있는 숫자의 경우의 수
    down = dice_list[0][i]
    up = dice_list[0][(i+3)%6]
    sum=0
    for k in range(6,0,-1):
        if k != down and k != up:
            max_val = k
            sum = max_val
            break

    for j in range(1,n):
        down=up
        idx = dice_list[j].index(down)
        up=dice_list[j][(idx+3)%6]
        for k in range(6,0,-1):
            if k != down and k != up:
                max_val = k  
                sum += max_val
                break
    sum_list.append(sum)

result = max(sum_list)
print(result)


# 18:20 중단