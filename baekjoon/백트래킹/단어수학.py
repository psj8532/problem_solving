#1339 #15:00
#앞에 있는 문자부터 0~9까지 하나씩 넣어보기
#앞에 있는 수가 정해지면 뒤에 있는 숫자는 나머지 숫자 중 하나
#visited 크기 10짜리 생성
import sys
sys.stdin=open("단어수학.text","r")

def getNum(word):
    for idx in range(10):
        if not visited[idx]:
            visited[idx]=word
            return

n=int(input())
data=[list(map(str,input())) for _ in range(n)]

alpha=[]
for i in range(n):
    for j in data[i]:
        if j not in alpha:
            alpha.append(j)
while
num_list=list(range(0,10))
for i in num_list:








# for i in range(10):
#     visited = [0] * 10
#     visited[i]=alpha[0]
#     for j in range(1,len(alpha)):
#         getNum(alpha[j])
#
#     print(*visited)
#     max_val=0
#     sum_val=0
#     for i in range(n):
#         val = 0
#         for j in data[i]:
#             val= val*10+visited.index(j)
#         sum_val+=val
#     if max_val<sum_val:
#         max_val=sum_val
# print(max_val)