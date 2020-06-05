# Z

> 풀이방법

- 재귀를 이용한 분할 정복
- 2^1 크기가 됬을때 이중 for문을 돌려서 갯수를 카운트해나감



> 오류

- 메모리 초과
  - 갯수를 이차원 리스트에 저장하여 메모리 초과 발생
    - 갯수를 카운트한 변수만을 이용
- 시간 초과
  - 계속 분할하면서 마지막에 for문을 다 돌리는 것이 원인인듯하다
  - 기존의 코드는 모든 사분면을 파고 들어가면서 분할 정복



> 개선 방안

- 모든 사분면을 탐색할 필요없이 범위 안에 해당하는 사분면만 분할정복

- 행,열의 범위는 m을 기준으로 범위를 나눌 수 있음
- 범위를 계산해서 필요하지 않은 사분면은 재귀를 타지 않고 바로 갯수를 더해서 넘어감
  - 갯수를 더할땐 2^(n-1)*2^(n-1)개임을 이용
- 2^11 기준 2.4초에서 0.00023초까지 줄였음
- Python,pypy 모두 통과



> 코드

```python
def div(n,sy,sx):
    global cnt,flag
    m = 2**(n-1)
    if n == 0:
        flag = True
        return
    for i in range(2):
        for j in range(2):
            if sy+m*i <= r < sy+m*(i+1) and sx+m*j <= c < sx+m*(j+1):
                div(n-1, sy+m*i, sx+m*j)
                if flag: return
            else:
                cnt = cnt+m*m

N,r,c = map(int,input().split())
cnt = 0
flag = False
div(N,0,0)
print(cnt)
```

