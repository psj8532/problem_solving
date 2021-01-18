N = int(input())
peoples = list(map(int,input().split()))
peoples.sort()
answer = 0
for i in range(N):
    answer += peoples[i] * (N-i)
print(answer)