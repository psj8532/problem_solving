M = int(input())
shingles = list(map(int,input().split()))
K = int(input())
total = sum(shingles)
answer = 0
for shingle in shingles:
    sum_val = 1
    for cnt in range(K):
        val = (shingle - cnt) / (total-cnt)
        sum_val *= val
    answer += sum_val
print(answer)