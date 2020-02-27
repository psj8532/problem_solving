#6603 #15:19
#입력이 0 하나 나올때까지 while문으로 입력받기
# data[0]: 집합의 원소가 몇개인지
# data[1]~:집합안에 들어있는 숫자
# 순열 이용
# in_perm 대신 집합안에 있는 수를 이용
# in_perm true 만들때 a[i]가 들어있는 인덱스 찾고 거기를 true로 변환
import sys
sys.stdin = open("로또.text","r")

# def perm(a,k):
#     if k==6:
#         print(*a)
#     else:
#         in_perm = [False]*n
#         for i in range(k):
#             in_perm[s.index(a[i])] = True
#         for i in range(n-1,-1,-1):
#             if in_perm[i]:
#                 posi = i
#                 break
#         else:
#             posi=0
#         cnt=0
#         c=[0]*n
#         for i in range(posi,n):
#             if in_perm[i] == False:
#                 c[cnt] = s[i]
#                 cnt+=1
#
#         for i in range(cnt):
#             a[k]=c[i]
#             perm(a,k+1)
# tc=0
# data=[]
# while 1:
#     data.append(list(map(int,input().split())))
#     if len(data[tc])==1 and not data[tc][0]:
#         break
#     tc+=1
#
# for t in range(tc):
#     n = data[t][0]
#     a=[0]*6
#     s=[]
#     for idx in range(1,1+n):
#         s.append(data[t][idx])
#     perm(a,0)
#     print()
# #16:40


# #성민이형이 수정 요청한 코드
# def lotto(Arr):
#     if len(Stack) == 6:   #숫자 6개가 채워지면 Result에 넣고 함수 끝냄
#         Temp = Stack[:]
#         Result.append(Temp)
#         return
#
#     for i in range(0, len(Arr)):      #수정 요망
#         # if not Stack:                 #Stack에 숫자 암것도 안들어가있을때 조건이 필요해서
#         #     Stack.append(Arr[i])      #if elif로 나눴는데 1개로 깔끔하게 합칠 수 있는지
#         #     lotto(Arr)
#         #     Stack.pop()
#                                       #반복할때 남은 숫자 다 넣어도 Stack 길이가 6이 안될때에는 탐색 안함
#         if not Stack or (Arr[i] not in Stack and Arr[i] > Stack[-1] and len(Arr)-i >= 6 - len(Stack)):
#             Stack.append(Arr[i])
#             lotto(Arr)
#             Stack.pop()
#
# keepgoing = True
# while keepgoing:
#     Inputarr = list(map(int, input().split())) #입력받은 리스트
#     Result = []                                #6개 로또 숫자열을 하나 완성하면 Result안에 넣어둘 예정
#     k = Inputarr[0]
#     if k == 0:                                 #0이 입력되면 반복문 끝냄
#         break
#     Inputarr = Inputarr[1:]
#     Stack = []                                 #로또 숫자열
#
#     lotto(Inputarr)
#     for i in Result:
#         for j in i:
#             print(j, end=' ')
#         print()
#     print()
