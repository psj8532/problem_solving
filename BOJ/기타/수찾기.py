N = int(input())
table = list(map(int,input().split()))
M = int(input())
numbers = list(map(int,input().split()))

table = sorted(table)
for num in numbers:
    answer = 0
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if table[mid] > num:
            right = mid - 1
        elif table[mid] == num:
            answer = 1
            break
        else:
            left = mid + 1
    print(answer)