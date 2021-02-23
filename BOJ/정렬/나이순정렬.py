N = int(input())
info = []
for i in range(N):
    age, name = input().split()
    info.append([int(age),name,i])
info = sorted(info, key=lambda x:(x[0],x[2]))
for row in info:
    print(*row[:2])