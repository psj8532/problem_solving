# import sys
# sys.stdin = open("3975.text","r")
result = []
t=int(input())
for tc in range(1,t+1):
    data=list(map(int,input().split()))
    alice_num = data[0] / data[1]
    bob_num = data[2] / data[3]

    if alice_num == bob_num:
        result.append('DRAW')
    elif alice_num > bob_num:
        result.append('ALICE')
    else:
        result.append('BOB')

for i in range(1,t+1):
    print('#{} {}'.format(i,result[i-1]))