#2210 #18:11
#visit 안써도됨
#result에 문자열 저장
#문자들을 추가
#다섯번 이동 #여섯자리 만들어지면 result리스에 있는지 확인
def dfs(y,x,depth,word):
    depth+=1
    word+=matrix[y][x]
    if depth==6 and word not in result:
        result.append(word)
        # print(*result)
        return
    elif depth==6:
        return
    for dir in range(len(dy)):
        new_y=y+dy[dir]
        new_x=x+dx[dir]
        if 0<=new_y<5 and 0<=new_x<5:
            dfs(new_y,new_x,depth,word)
    return
matrix=[]
result=[]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
for _ in range(5):
    matrix.append(list(map(str,input().split())))
for i in range(5):
    for j in range(5):
        text=''
        dfs(i,j,0,text)
print(len(result))
#19:14