N = int(input())
alpha = {}
for i in range(N):
    word = input()
    for idx,ch in enumerate(word):
        if ch in alpha:
            alpha[ch] += 10**(len(word) - idx - 1)
        else:
            alpha[ch] = 10**(len(word) - idx - 1)

alphas = []
for k in alpha:
    alphas.append([k,alpha[k]])
alphas.sort(reverse=True ,key=lambda x:x[1])

answer = 0
digit = 9
for lst in alphas:
    ch, num = lst
    answer += digit * num
    digit -= 1

print(answer)

