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

---

### heapq

```python
import heapq
```

#### 기존 리스트를 heap으로 변환

```python
h = [3,1,10]
heapq.heapify(h)
print(h)
# [1, 3, 10]
```

#### heap에 원소 추가

```python
h = [3,1,10]
heapq.heappush(h, 5)
print(h)
# [1, 3, 5, 10]
```

#### heap 최솟값 확인 및 추출

```python
# 추출
heapq.heappop(h)
# 값만 확인
print(heap[0])
```

#### 최대힙

```python
import heapq

s = [3, 1, 7, 5]
heap = []

for n in s:
  heapq.heappush(heap, (-n, n))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```

```python
import heapq

s = [3, 1, 7, 5]
heap = []

for n in s:
  heapq.heappush(heap, -n) 

while heap:
  print(heapq.heappop(heap))  # 뽑아서 -붙여주면 최댓값으로 추출 가능
```



## JavaScript

### 비트를 이용한 연산

##### 소숫점 버림

> ~~

```javascript
n = 10.12;
console.log(~~n);
// 10
```

##### 인덱스 요소 검사

> ~ 
>
> 없으면 -1이 반환되고, -1의 ~은 0임을 이용

```javascript
str = 'abcd';
str.indexOf('q'); // -1
~str.indexOf('q'); // 0
!~str.indexOf('q'); // 1
```

---

### 2차원 배열 생성

```javascript
const create2DArray = (rows,columns) => {
  const arr = new Array(rows);
  for (let i = 0; i < rows; i++) {
    arr[i] = new Array(columns).fill(0);
  }
  return arr;
}

const arr = create2DArray(5,2);
```

---

### 문자열 <=> 숫자

##### 문자열 => 숫자열

- 숫자로 이루어진 문자열에 1을 곱함
- 숫자로 이루어진 문자열에 `+` 기호 사용

```javascript
let s = '123'; // String
s = s*1; // Number
```

```javascript
let s = '123' // String
s = +s; // Number
```

##### 숫자 => 문자열

- **문자열 + 숫자 = 문자열** 로 자동 형변환

```javascript
let num = 10; // Number
num = ''+num; // String
```

---

### 알고리즘

##### 조합

```javascript
const combination = (k, a, cSize, totalSize) => {
    if (k === cSize) {
        const temp = a.map(v => v);
        comb.push(temp);
        return;
    }
    const inComb = new Array(totalSize).fill(false);
    for (let i = 0; i < k; i++) {
        inComb[a[i]] = true;
    }
    let posi = 0;
    for (let i = totalSize - 1; i >= 0; i--) {
        if (inComb[i]) {
            posi = i + 1;
            break;
        }
    }
    const c = new Array(totalSize).fill(0);
    let cnt = 0;
    for (let i = posi; i < totalSize; i++) {
        if (!inComb[i]) {
            c[cnt++] = i;
        }
    }
    for (let i = 0; i < cnt; i++) {
        a[k] = c[i];
        combination(k + 1, a, cSize, totalSize);
    }
};
```

