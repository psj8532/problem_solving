N = int(input())
alphabets = {}
for _ in range(N):
    word = input()
    word_size = len(word)
    for idx, ch in enumerate(word):
        if ch in alphabets: alphabets[ch] += 10**(word_size - 1 - idx)
        else: alphabets[ch] = 10**(word_size - 1 - idx)

alphabet_list = []
for ch, indices in alphabets.items():
    alphabet_list.append([ch, indices])
sorted_alphabets = sorted(alphabet_list, reverse=True, key=lambda x:x[1])

answer, num = 0, 9
for ch, n in sorted_alphabets:
    answer += n * num
    num -= 1

print(answer)
