N, W, L = map(int,input().split())
trucks = list(map(int,input().split()))
front, back, weight, time = 0, 0, 0, 0
position = [0]*N
for i, truck in enumerate(trucks):
    isExcess = False
    while weight + truck > L:
        dist = W - position[front] + 1
        for j in range(front, back + 1):
            position[j] += dist
        weight -= trucks[front]
        front += 1
        isExcess = True
    back = i
    if isExcess:
        position[back] += 1
    else:
        for j in range(front, back+1):
            position[j] += 1
        time += 1
        if position[front] == W+1:
            weight -= trucks[front]
            front += 1
    weight += truck
time += W
print(time)