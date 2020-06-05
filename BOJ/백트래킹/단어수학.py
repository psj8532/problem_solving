import sys
sys.stdin=open("단어수학.text","r")

# 완탐이라서 시간초과 발생
# def get_num(index):
#     global max_val
#     if index == len(alpha):
#         val = 0
#         for y in range(N):
#             for x in range(len(data[y])):
#                 matrix[y][x] = num.index(data[y][x])
#             word = ''.join(map(str,matrix[y]))
#             word = int(word)
#             val += word
#         if val>max_val:
#             max_val = val
#         return
#     for j in range(9,-1,-1):
#         if num[j]==-1:
#             num[j] = alpha[index]
#             get_num(index+1)
#             num[j] = -1
#
# N = int(input())
# data = [list(input()) for _ in range(N)]
# c = [0]*128
# num = [-1]*10
# alpha = []
# max_val = 0
# matrix = []
# for i in range(N):
#     matrix.append([0]*len(data[i]))
#
# for i in range(N):
#     for j in range(len(data[i])):
#         if not c[ord(data[i][j])]:
#             alpha.append(data[i][j])
#             c[ord(data[i][j])] = 1
# get_num(0)
# print(max_val)
