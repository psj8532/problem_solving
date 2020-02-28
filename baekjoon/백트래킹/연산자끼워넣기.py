#14888 #17:19
#n:수의 갯수, n-1:수식의 갯수
import sys
sys.stdin=open("연산자끼워넣기.text","r")

def perm(a,k):
    if k==n-1:
        temp = a[:]
        result.append(temp)
    else:
        in_perm=[False]*(n-1)

        for i in range(k):
            inperm[]

max_val = 9876543210
min_val = -9876543210

n = int(input())
data = list(map(int,input().split()))
op_code = list(map(int,input().split()))
op_list = ['+']*op_code[0]
op_list += ['-']*op_code[1]
op_list += ['*']*op_code[2]
op_list += ['/']*op_code[3]
result=[]
op_data=[0]*(n-1)
perm(op_data,0,k)