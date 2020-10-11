# RGB거리

### 알고리즘

- DP



### 구현 방법

- 집에 칠해지는 색깔은 이전 집의 색깔에 따라 영향을 받으므로 현재 집에 칠할 색에 따라 이전 집에 칠해질 색을 정하는 방법으로 구현
  - 현재 집에 빨간색을 칠하면 이전 집의 색은 초록색과, 파랑색이 후보가 되는데 이 중 더 작은 값을 칠하는 것이 최소 비용이 됨
- i번째를 기준으로 dp[i-1]에는 그 색을 선택했을 때의 최소 비용만을 선택했을 때의 합이 저장되있음
- 마지막에 dp에서 최솟값이 곧 최소비용이 된다.



### 잘못 접근했던 생각

- 현재 집에서 칠할 색에 따라 다음 집을 칠할 색을 정해야한다는 생각에 빠져서 해결방법을 찾지 못함



### 참고

- 최솟값을 구하는 반복적인 과정을 일일이 모두 구현했던 것을 함수로 정의하여 정리했더니 맞았음
  - 함수로 정의해서 관리하는 것이 실수를 줄일 수 있고, 코드가 간결해짐



### 코드

```python
def get_some(a,b):
    if a <= b:
        return a
    else:
        return b


def solution(N):
    dp = [house[0][0],house[0][1],house[0][2]]
    for i in range(1,N):
        temp = [0,0,0]
        temp[0], temp[1], temp[2] = dp[0], dp[1], dp[2]
        temp[0] = house[i][0] + get_some(dp[1], dp[2])
        temp[1] = house[i][1] + get_some(dp[0], dp[2])
        temp[2] = house[i][2] + get_some(dp[0], dp[1])
        dp[0], dp[1], dp[2] = temp[0], temp[1], temp[2]
    return min(dp)


N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
print(solution(N))
```

