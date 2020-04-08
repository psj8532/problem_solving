import sys
sys.stdin=open("test1.txt","r")
from _collections import deque

def bfs(y,x,cnt):
    deq = deque() #deque를 이용
    deq.append((y,x))
    visited[y][x]=1 #(0,0) 방문했다는 표시 남김

    while deq:
        here = deq.popleft()
        y,x = here[0],here[1]
        for dir in range(len(direct)):
            new_y,new_x=y+direct[dir][0],x+direct[dir][1]
            if 0<=new_y<n and 0<=new_x<n and matrix[new_y][new_x] and not visited[new_y][new_x]:
                deq.append((new_y,new_x)) #범위를 벗어나지 않고, 먼지가 존재하며, 방문하지 않은 곳의 좌표를 deq에 추가
                visited[new_y][new_x]=1
                cnt+=matrix[new_y][new_x] #먼지 양 더해줌
    return cnt

direct=[(-1,0),(0,1),(1,0),(0,-1)] #4방향 탐색을 위한 방향 정보를 리스트에 저자
t=int(input()) #테스트 케이스의 갯수
for tc in range(1,t+1):
    n=int(input())
    matrix=[list(map(int,input().split())) for _ in range(n)] #
    visited=[[0]*n for _ in range(n)] #한번 방문 했던 곳은 다시 방문하지 않기 위해 2차원 리스트에 방문한 곳 표시
    count = bfs(0,0,matrix[0][0]) #bfs 함수를 이용하여 탐색, count에 총 먼지의 양 저장
    print('#{} {}'.format(tc,count))