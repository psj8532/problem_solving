N = int(input())
ropes = [int(input()) for _ in range(N)]
sorted_ropes = sorted(ropes)
answer = 0
for start in range(N):
    weight = sorted_ropes[start] * (N - start)
    if weight > answer: answer = weight
print(answer)