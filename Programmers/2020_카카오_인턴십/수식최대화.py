def perm(index,l,a,s):
    if index == l:
        temp = a[:]
        s.append(temp)
    else:
        in_perm = [False]*l
        for i in range(index):
            in_perm[a[i]] = True
        c = [0]*l
        cnt = 0
        for i in range(l):
            if not in_perm[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[index] = c[i]
            perm(index+1,l,a,s)


def solution(expression):
    answer = 0
    number = ''
    numbers = []
    operator = dict()
    for ch in expression:
        if ch.isdigit():
            number += ch
        else:
            numbers.append(int(number))
            number = ''
            numbers.append(ch)
            if ch not in operator:
                operator[ch] = len(operator)
    numbers.append(int(number))
    a = [0]*len(operator)
    s = []
    perm(0,len(operator),a,s)
    for r in range(len(s)):
        sum = 0
        stack = []
        new_nums = []
        for n in numbers:
            if n == '+' or n == '-' or n == '*':
                if not stack:
                    stack.append(n)
                else:
                    while stack:
                        if s[r].index(operator[stack[len(stack)-1]]) <= s[r].index(operator[n]):
                            new_nums.append(stack.pop())
                        else:
                            break
                    stack.append(n)
            else:
                new_nums.append(n)
        while stack:
            new_nums.append(stack.pop())

        
    return answer
    # return numbers

print(solution(input()))

