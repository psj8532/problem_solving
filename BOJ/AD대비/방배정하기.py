def check(index,sum):
    global isSuccess
    if isSuccess: return
    if index == 3: return
    for i in range(room[3]//room[index]+1):
        if sum + room[index] * i == room[3]:
            isSuccess = True
            return
        elif sum + room[index] * i > room[3]:
            return
        else:
            check(index+1,sum+room[index]*i)


room = list(map(int,input().split()))
isSuccess = False
check(0,0)
if isSuccess:
    print(1)
else:
    print(0)