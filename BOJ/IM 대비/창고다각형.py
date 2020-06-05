#창고 다각형 # 20:09
column=int(input())


L=[]
H=[]
for i in range(column):
    l, h = map(int,input().split())
    L.append(l)
    H.append(h)
result=H.index(max(H))
L[result] # 최고 높이를 가지고 있는 L위치 찾기



# data = [[] for _ in range(column)]
# for i in range(column):
#     data[i] = list(map(int,input().split())) # data[0]: 위치, data[1]: 높이
# h_max = data[0][1]
# for i in range(1, column):
#     if h_max < data[i][1]:
#         h_max = data[i][1]
# print()