#2661 #16:14
# import sys
# sys.stdin=open("좋은수열.text","r")

def arrNum(number):
    temp=number
    count=0
    while temp:
        temp//=10
        count+=1
    temp=number
    num_list=[0]*count
    for i in range(count-1,-1,-1):
        num_list[i]=temp%10
        temp//=10
    return num_list

def getSome(arr):
    c=len(arr)
    for i in range(1,c-1):
        for j in range(c-i+1):
            for x in range(j,j+i):
                if arr[x]==arr[x+1]:
                    return False
    return True

def perm(col,val):
    if col==n:
        global min_val
        if min_val>val:
            min_val=val
    else:
        for next_num in range(1,4):
            a=arrNum(val*10+next_num)
            if getSome(a):
                perm(col+1,val*10+next_num)


n=int(input())
min_val=987654321
for num in range(1,4):
    a=arrNum(num)
    if getSome(a):
        perm(1,num)
print(min_val)