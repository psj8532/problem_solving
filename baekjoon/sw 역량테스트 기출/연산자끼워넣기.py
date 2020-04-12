import sys
sys.stdin = open("연산자끼워넣기.txt","r")

def perm(a,k):
    if k==n-1:
        temp = a[:]
        s.append(temp)
    else:
        in_perm=[False]*(n-1)
        for i in range(k):
            in_perm[a[i]]=True
        c=[0]*(n-1)
        cnt = 0
        for i in range(n-1):
            if not in_perm[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[k] = c[i]
            perm(a,k+1)

def calculator(r):
    val = num_list[0]
    for c in range(1,n):
        x = num_list[c]
        opcode = operator[s[r][c-1]]
        val = calculus(val,x,opcode)
    return val

def calculus(new_y,new_x,op):
    if op=='+':
        return new_y+new_x
    elif op=='-':
        return new_y-new_x
    elif op=='*':
        return new_y*new_x
    else:
        if new_y>0:
            return new_y//new_x
        else:
            new_y=-new_y
            return -(new_y//new_x)

n = int(input())
num_list = list(map(int,input().split()))
operator_list = list(map(int,input().split()))
operator = []
max = -9876543210
min = 9876543210
for op in range(4):
    if operator_list[op]>0 and op==0:
        while operator_list[op]:
            operator.append('+')
            operator_list[op]-=1
    elif operator_list[op]>0 and op==1:
        while operator_list[op]:
            operator.append('-')
            operator_list[op]-=1
    elif operator_list[op]>0 and op==2:
        while operator_list[op]:
            operator.append('*')
            operator_list[op]-=1
    elif operator_list[op] > 0 and op == 3:
        while operator_list[op]:
            operator.append('//')
            operator_list[op]-=1
a = [0]*(n-1)
s = []
perm(a,0)
m=len(s)

for i in range(m):
    result = calculator(i)
    if result>max:
        max = result
    if result<min:
        min = result
print(max)
print(min)