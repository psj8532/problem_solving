#08:02
def change(i,j,c):
    cnt=0
    for y in range(i,i+8,2):
        for x in range(j,j+8,2):
            if matrix[y][x]!=c:
                cnt+=1
            if matrix[y][x+1]==c:
                cnt+=1
            if matrix[y+1][x]==c:
                cnt+=1
            if matrix[y+1][x+1]!=c:
                cnt+=1
    return cnt

n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(input()))
min_val=987654321
for i in range(n-8+1):
    for j in range(m-8+1):
        for color in ['W', 'B']:
            cnt = change(i,j,color)
            if cnt < min_val:
                min_val = cnt
print(min_val)
#08:47