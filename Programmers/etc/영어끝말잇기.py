# 15:52 ~ 16:10
def solution(n, words):
    answer = [0,0]
    check = {words[0]:1}
    for i in range(1,len(words)):
        word = words[i]
        if words[i-1][-1] != word[0] or word in check:
            cnt = i // n + 1
            number = i % n + 1
            answer = [number,cnt]
            break
        else:
            check[word] = 1
    return answer

# n	words	result
ex1 = (3,	['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'])	# [3,3]
ex2 = (5,	['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'])	# [0,0]
ex3 = (2,	["hello", "one", "even", "never", "now", "world", "draw"])	# [1,3]
print(solution(*ex3))
