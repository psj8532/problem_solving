# 다음과 같이 import를 사용할 수 있습니다.
# import math
from collections import deque

def solution(garden):
    # 여기에 코드를 작성해주세요.
    def bfs():
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        while deq:
            y, x, depth = deq.popleft()
            for dir in range(4):
                ny, nx = y + dy[dir], x + dx[dir]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and not garden[ny][nx]:
                    deq.append([ny, nx, depth + 1])
                    visited[ny][nx] = 1
        return depth

    answer, N = 0, len(garden)
    visited = [[0] * N for _ in range(N)]
    cand = []
    for i in range(N):
        for j in range(N):
            if garden[i][j]:
                cand.append([i, j, 0])
                visited[i][j] = 1
    deq = deque(cand)
    return bfs()


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")