# 10:40 ~ 10:46
def solution(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack: return False
            stack.pop()

    return not stack

# s	answer
ex = [
    "()()",	# true
    "(())()",	# true
    ")()(",	# false
    "(()("	# false
]
for t in ex:
    print(solution(t))