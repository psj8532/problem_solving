def rangeCheck(new_y,new_x,d):
    if d==1:
        new_x+=1
    elif d==2:
        new_x-=1
    elif d==3:
        new_y-=1
    else:
        new_y+=1

    if 0<=new_y<n and 0<=new_x<m:
        return new_y,new_x
    else:
        return -10,-10

def diceMove(d):
    if d==1:
        Dice[1][1],Dice[1][2],Dice[3][1],Dice[1][0]=Dice[1][0],Dice[1][1],Dice[1][2],Dice[3][1]
    elif d==2:
        Dice[1][0], Dice[1][1], Dice[1][2], Dice[3][1] = Dice[1][1], Dice[1][2], Dice[3][1], Dice[1][0]
    elif d==3:#인덱스 값 잘못 입력
        Dice[3][1], Dice[2][1], Dice[1][1], Dice[0][1] = Dice[0][1], Dice[3][1], Dice[2][1], Dice[1][1]
    elif d==4:
        Dice[1][1], Dice[2][1], Dice[3][1], Dice[0][1] = Dice[0][1], Dice[1][1], Dice[2][1], Dice[3][1]
    print(Dice[1][1])
    return Dice[3][1]

def bottomCheck(b,new_y,new_x):
    if not Matrix[new_y][new_x]:
        Matrix[new_y][new_x]=b
    else:
        Dice[3][1]=Matrix[new_y][new_x]
        Matrix[new_y][new_x]=0 #복사하고 0으로 안바꿔줬음

n,m,y,x,k=map(int,input().split())
Matrix=[list(map(int,input().split())) for _ in range(n)]
Data=list(map(int,input().split()))
Dice=[[0]*3 for _ in range(4)]#문제에 나와있는 주사위 초기값을 확인하지 못했음

for i in range(k):
    ty,tx=y,x
    y,x = rangeCheck(y,x,Data[i])
    if (y,x)==(-10,-10):
        y,x=ty,tx
        continue
    bottom = diceMove(Data[i])
    bottomCheck(bottom,y,x)