def pseudo_palindrome(left, right):
    if left == right: return False
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left + 1, right - 1
    return True

def check_palindrome(l, r):
    left, right = l, r
    while left < right:
        if word[left] != word[right]:
            is_palindrome = pseudo_palindrome(left + 1, right)
            if is_palindrome: return 1
            is_palindrome = pseudo_palindrome(left, right - 1)
            if is_palindrome: return 1
            return 2
        left, right = left + 1, right - 1
    return 0

T = int(input())
for tc in range(T):
    word = input()
    word_size = len(word)
    answer = check_palindrome(0, word_size - 1)
    print(answer)