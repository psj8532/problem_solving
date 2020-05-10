import sys
sys.stdin = open("신기한소수.txt","r")
#에라토스테네스의 체
def solve(index, word):
    if index == N+1:
        number = int(word)
        result.append(number)
        return
    val = word[:index+1]
    val = int(val)
    n = int(val**0.5)
    for j in range(2, n+1):
        if not (val % j):
            return
    solve(index+1, word)

N = int(input())
result = []
for num in range(2*(10**(N-1)),10**N):
    word = str(num)
    solve(0, word)
result.sort()
for i in range(len(result)):
    print(result[i])