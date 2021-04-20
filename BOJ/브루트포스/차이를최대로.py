from itertools import permutations

def calculate(new_arr):
    val = 0
    for i in range(N-1):
        val += abs(new_arr[i] - new_arr[i+1])
    return val

N = int(input())
arr = list(map(int,input().split()))
answer = -9876543210
perm = list(map(list,permutations(arr, N)))
for p in perm:
    answer = max(answer, calculate(p))
print(answer)