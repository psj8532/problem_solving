import sys
sys.stdin = open("구슬탈출2.txt","r")
from _collections import deque
# 한킨씩 이동하는게 아니라 쭉 굴리는 것이다
# 구슬이 한 칸에 같이 있을 수 없다
# 10턴이 지나면 -1
def bfs(red,blue):
    cnt_r = cnt_b = 1
    count_r = count_b = 0
    while cnt_r:
        while cnt_b:
            here = blue.popleft()
            y,x = here[0],here[1]
            cnt_b -= 1
            for dir in range(4):
                new_y,new_x = y+direct[dir][0],x+direct[dir][1]
                if matrix[new_y][new_x]=='O':
                    return -1
                elif matrix[new_y][new_x]=='.' and not visited_b[new_y][new_x]:
                    blue.append((new_y,new_x))
                    count_b += 1
        while cnt_r:
            here = red.popleft()
            y, x, d = here[0], here[1], here[2]
            cnt_r -= 1
            for dir in range(4):
                new_y, new_x = y + direct[dir][0], x + direct[dir][1]
                if matrix[new_y][new_x] == 'O':
                    return d+1
                elif matrix[new_y][new_x] == '.' and not visited_r[new_y][new_x] and not (new_y,new_x) in blue:
                    red.append((new_y, new_x, d + 1))
                    count_r += 1
        cnt_r,cnt_b = count_r,count_b
        count_r = count_b = 0
    return -1

direct = [(-1,0),(0,1),(1,0),(0,-1)]
N,M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
visited_b = [[0]*M for _ in range(N)]
visited_r = [[0]*M for _ in range(N)]
red = deque()
blue = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j]=='R':
            visited_r[i][j] = 1
            red.append((i,j,0))
        elif matrix[i][j]=='B':
            visited_b[i][j] = 1
            blue.append((i,j))
result = bfs(red,blue)
print(result)
