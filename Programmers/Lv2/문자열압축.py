def solution(s):
    answer = S = len(s)
    half = S // 2
    for cutting in range(1, half + 1):
        words = {}
        word_key = []
        ns = ''
        for i in range(0, S, cutting):
            word = s[i:i+cutting]
            if word_key and word_key[-1] == word:
                words[word] += 1
            else:
                if word_key and word_key[-1] != word:
                    prev_word = word_key.pop(0)
                    if words[prev_word] == 1: ns += prev_word
                    else: ns += str(words[prev_word]) + prev_word
                    del words[prev_word]
                word_key.append(word)
                words[word] = 1
        if word_key:
            last_word = word_key.pop(0)
            if words[last_word] == 1: ns += last_word
            else: ns += str(words[last_word]) + last_word
        answer = min(answer, len(ns))
    return answer