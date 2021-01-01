def solution(expression):
    answer = 0
    lst = []
    op_set = set()
    n = ''
    for ch in expression:
        if ch.isdigit():
            n += ch
        else:
            n = int(n)
            lst.append(n)
            lst.append(ch)
            op_set.add(ch)
            n = ''
    lst.append(int(n))
    op_cnt = len(op_set)
    def perm(index):
        if index == op_cnt:
            temp = a[:]
            s.append(temp)
        else:
            in_perm = [False] * op_cnt
            for i in range(index):
                in_perm[a[i]] = True
            c = [0] * op_cnt
            cnt = 0
            for i in range(op_cnt):
                if not in_perm[i]:
                    c[cnt] = i
                    cnt += 1
            for i in range(cnt):
                a[index] = c[i]
                perm(index+1)

    s = []
    a = [0] * op_cnt
    perm(0)

    op_lst = []
    while op_set:
        op_lst.append(op_set.pop())

    def operator(x,y,o):
        if o == '+':
            return x + y
        elif o == '-':
            return x - y
        else:
            return x * y


    for i in range(len(s)):
        # 숫자가 클수록 우선순위 높음
        opcode = {}
        for j in range(len(s[i])):
            opcode[op_lst[s[i][j]]] = j
        num_stack = []
        op_stack = []
        for op in lst:
            if type(op) == int:
                num_stack.append(op)
            else:
                # 연산자 비교
                if not op_stack:
                    op_stack.append(op)
                elif opcode[op_stack[-1]] < opcode[op]: # 들어오는 연산자의 우선순위가 더 높다면
                    op_stack.append(op)
                else:
                    while op_stack and opcode[op_stack[-1]] >= opcode[op]:
                        nop = op_stack.pop()
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        result = operator(num1,num2,nop)
                        num_stack.append(result)
                    op_stack.append(op)
        while op_stack:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            nop = op_stack.pop()
            result = operator(num1,num2,nop)
            num_stack.append(result)
        result = abs(num_stack.pop())
        answer = max(result,answer)

    return answer

ex1 = "100-200*300-500+20" # 60420
ex2 = "50*6-3*2" # 300
print(solution(ex1))