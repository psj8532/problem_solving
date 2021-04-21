N = int(input())
products = [int(input()) for _ in range(N)]
products = sorted(products, reverse=True)
answer = 0
for idx, price in enumerate(products):
    if (idx + 1) % 3: answer += price
print(answer)