from itertools import combinations

alphabets = list(map(lambda x:chr(x), list(range(ord('a'), ord('z') + 1))))
essential_word = ['a', 'c', 'i', 'n', 't']
E = len(essential_word)
for ch in essential_word:
    alphabets.pop(alphabets.index(ch))
N, K = map(int,input().split())
words = [input() for _ in range(N)]
answer = 0
if K < E:
    print(answer)
else:
    comb = list(map(list, combinations(alphabets, K - E)))
    for c in comb:
        new_comb = essential_word + c
        readable_word = 0
        for word in words:
            for i in range(4, len(word) - 4):
                if word[i] not in new_comb: break
            else:
                readable_word += 1
        if readable_word > answer: answer = readable_word
    print(answer)