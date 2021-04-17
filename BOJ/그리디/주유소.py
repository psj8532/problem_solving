N = int(input())
distance = list(map(int,input().split()))
cities = list(map(int,input().split()))

min_price, acc_dist, answer = cities[0], 0, 0
for i in range(N-1):
    price, dist = cities[i], distance[i]
    if min_price > price:
        answer += acc_dist * min_price
        acc_dist, min_price = dist, price
    else:
        acc_dist += dist
else:
    if acc_dist:
        answer += acc_dist * min_price
print(answer)