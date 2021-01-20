# 11:47 ~ 12:54
def check(ts):
    stack = []
    for ch in ts:
        if not stack and ch == ')':
            return False
        elif ch == ')':
            t = stack.pop()
            if t == ch:
                return False
        else:
            stack.append(ch)
    if stack: return False
    else: return True

def divide(w):
    op = 0
    cl = 0
    a = ''
    for idx,ch in enumerate(w):
        if ch == '(':
            op += 1
        else:
            cl += 1
        a += ch
        if op and op == cl:
            b = w[idx + 1:]
            # print('a: ', a, 'b: ', b)
            return a, b
    b = ''
    return a, b

def solution(p):
    def recursion(w):
        if not w: return ''
        # u,v로 나누기
        u, v = divide(w)
        # u가 올바른 괄호 문자열이라면
        # print('u: ', u, 'v: ', v)
        if check(u):
            return u + recursion(v)
        # u가 올바른 괄호 문자열이 아니라면
        else:
            s = '(' + recursion(v) + ')'
            for i in range(1,len(u)-1):
                if u[i] == '(':
                    s += ')'
                else:
                    s += '('
            return s

    answer = ''
    # 분할: w => u,v
    answer = recursion(p)
    return answer

ex1 = "(()())()" # "(()())()"
ex2 = ")(" # "()"
ex3 = "()))((()" # "()(())()"
print(solution(ex3))