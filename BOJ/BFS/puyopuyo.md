# PuyoPuyo

> 아이디어

- 현재 턴에서 터뜨릴 수 있는 것들을 bfs로 찾아 터뜨림
- 한번이라도 떠뜨린다면 정렬하고 다음 턴 진행
- 한번도 터뜨리지 못하면 게임 종료



> 구현 방법

- 현재 턴에서 터뜨릴 수 있는 것들을 찾을 때는 bfs이용
  - queue를 이용하는데 저장했던 좌표들을 재사용해야하므로 pop하는 대신 front를 이용하여 값만 추출
  - 갯수가 4개 이상이면 queue에 있던 값들을 꺼내서 빈칸으로 바꿔줌
  - 정렬해야한다는 것을 알려야하므로 isEnd를 false로 바꿈
- 정렬(check)
  - 행을 우선적으로 탐색하여 .을 한개라도 만난 상태에서 문자를 만나게 된다면 change 함수 실행
- 정렬(change)
  - y,x 좌표들을 받아와서 y값과 y+1의 값을 바꿀 수 있다면 바꿔나감



> 오류

- 18%에서 틀렸는데 이는 change에서 0행에서 시작할 때 while문을 들어가지 못하여 오류 발생



> 코드

```python
def change(y,x):
    ny = y
    while 0<=ny<11 and matrix[ny+1][x] == '.':
        matrix[ny][x],matrix[ny+1][x] = matrix[ny+1][x],matrix[ny][x]
        ny += 1


def check():
    for c in range(6):
        flag = False
        for r in range(11,-1,-1):
            if matrix[r][c] != '.' and flag:
                change(r,c)
            elif matrix[r][c] == '.':
                flag = True


def bfs(y,x,c):
    global isEnd
    queue = []
    front = 0
    visited = [[0] * 6 for _ in range(12)]
    queue.append((y,x))
    visited[y][x] = 1
    while front != len(queue):
        here = queue[front]
        y,x = here[0],here[1]
        for dir in range(4):
            ny,nx = y+direct[dir][0],x+direct[dir][1]
            if 0<=ny<12 and 0<=nx<6 and matrix[ny][nx] == c and not visited[ny][nx]:
                queue.append((ny,nx))
                visited[ny][nx] = 1
        front += 1
    if front>=4:
        for idx in range(front):
            ny,nx = queue[idx][0],queue[idx][1]
            matrix[ny][nx] = '.'
        isEnd = False


matrix = [list(input()) for _ in range(12)]
direct = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
isEnd = False
while not isEnd:
    isEnd = True
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.':
                bfs(i,j,matrix[i][j])
    if not isEnd:
        cnt += 1
        check()
print(cnt)
```



