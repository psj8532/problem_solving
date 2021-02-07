# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(K, words):
    # 여기에 코드를 작성해주세요.
    answer, remainder = 1, K
    for word in words:
        l = len(word)
        if l > remainder:
            answer += 1
            remainder = K - l - 1
        else:
            remainder -= (l + 1)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")