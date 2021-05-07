N, M = map(int, input().split())
numbers = list(map(int, input().split()))
left = right = 0
answer = sum_val = 0
while left < N and right < N:
    sum_val += numbers[right]
    while sum_val >= M:
        if sum_val == M:
            answer += 1
        sum_val -= numbers[left]
        left += 1
    right += 1
print(answer)