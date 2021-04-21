## 풀이

처음 풀때는 문제가 이해되지 않아 오래걸리고 비효율적으로 풀었다. 하지만 두번째 풀때는 위키백과에 나온 설명을 잘 읽어보면서 이해했다.



#### 아이디어

내림차순으로 정렬한 후, i번째까지는 i개가 있고 이 값들은 모두 [i]보다 큰 값이다. [5,4,3,2,1]이 있다고 해보자. index가 1부터 시작한다고 생각했을 때, index가 3은 [3] 이상인 값이 3개이다. index가 4는 값이 2이기 때문에 4이상이 아니다. 따라서 H-Index를 만족하지 못한다. 이런식으로 index를 처음부터 끝까지 for문으로 돌리면서 조건을 만족하는 최대한 큰 값을 찾아내면 된다. 



## 코드

```javascript
const solution = (citations) => {
    let hIndex = 0;
    const newCitations = citations.sort((a, b) => b - a);
    for (let index = 0; index < newCitations.length; index++) {
        if (newCitations[index] > index) {
            hIndex = index + 1;
        } else {
            break;
        }
    }
    return hIndex;
};
```

```python
# 13:47 ~ 15:15
# 문제 설명 부실해서 오래걸림
def solution(citations):
    citations.sort(reverse=True)
    max_val = 0
    for idx in range(len(citations)):
        h = idx+1
        rear = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                rear += 1
            else:
                break
        if rear >= h and len(citations)-rear <= h:
            max_val = max(max_val, h)
    return max_val

ex1 = [3, 0, 6, 1, 5]	# 3
ex2 = [0,3,3,3,5,7]
ex3 = [0,3,3,3,5,5,7,9,10]
ex4 = [1,1,1,1,1]
ex5 = [25, 8, 5, 3, 3]
ex6 = [10, 8, 5, 4, 3]
ex7 = [13,12,11,10]
print(solution(ex1))
```

