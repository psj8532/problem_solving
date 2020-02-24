#15:40
# import sys
# sys.stdin=open("분해합.text","r")
#num을 1부터 1씩 증가시키면서 그 수의 분해합을 해서 n이 되는지 확인
#num이 n과 같아지면 생성자가 없는 것이므로 0을 출력

def array(val):
    temp = val
    result=0
    while temp:
        result += temp%10
        temp//=10
    return result
n=int(input())
num=1
IsEnd = False
while n!=num:
    num_sum = array(num)
    if num_sum+num == n:
        IsEnd = True
        break
    num+=1

if IsEnd:
    print(num)
else:
    print(0)
