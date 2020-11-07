#메모리초과
N = int(input())
answer = []
for _ in range(N):
    answer.append(int(input()))
answer.sort()
for num in answer:
    print(num)