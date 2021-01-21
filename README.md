## Python

### Itertool

- 직접 순열,조합을 만들 때보다 속도가 빠르다.

| 이터레이터                                                   | 인자                 | 결과                                                         |
| :----------------------------------------------------------- | :------------------- | :----------------------------------------------------------- |
| [`product()`](https://python.flowdas.com/library/itertools.html#itertools.product) | p, q, ... [repeat=1] | 데카르트 곱(cartesian product), 중첩된 for 루프와 동등합니다 |
| [`permutations()`](https://python.flowdas.com/library/itertools.html#itertools.permutations) | p[, r]               | r-길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음          |
| [`combinations()`](https://python.flowdas.com/library/itertools.html#itertools.combinations) | p, r                 | r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음               |
| [`combinations_with_replacement()`](https://python.flowdas.com/library/itertools.html#itertools.combinations_with_replacement) | p, r                 | r-길이 튜플들, 정렬된 순서, 반복되는 요소 있음               |

#### 중복 조합

```python
from itertools import product
product('ABCD', repeat=2)
# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
```

#### 순열

```python
from itertools import permutations
permutations('ABCD', 2)
# AB AC AD BA BC BD CA CB CD DA DB DC
```

#### 조합

```python
from itertools import combinations
combinations('ABCD', 2)
# AB AC AD BC BD CD
```

#### 조합 (요소 반복있는 경우)

```python
from itertools import combinations_with_replacement
combinations_with_replacement('ABCD', 2)
# AA AB AC AD BB BC BD CC CD DD
```

----

### Collections

#### Counter

```python
from collections import Counter
s = ['a','a','b']
Counter(s)
# Counter({'a': 2, 'b': 1})
```

#### Deque

- 링크드리스트 구조

```python
from collections import deque

deq = deque([10,5,7])

# 삽입
deq.appendleft()
deq.append()
# 중간에 삽입
deq.insert(idx, num)
# 삭제
deq.popleft()
deq.pop()
# 조회
deq[0]
```



## JavaScript

### 비트를 이용한 연산

#### ~~

- 소숫점 버림

```javascript
n = 10.12;
console.log(~~n);
// 10
```

#### ~

- 인덱스 요소 검사

```javascript
str = 'abcd';
str.indexOf('q'); // -1
~str.indexOf('q'); // 0
!~str.indexOf('q'); // 1
```



