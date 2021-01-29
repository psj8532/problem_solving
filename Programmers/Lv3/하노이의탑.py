def solution(n):
    def hanoi(cur, target, sub, num):
        if num == 1:
            answer.append([cur, target])
            print('num: ', num)
            print(cur,target)
            return
        hanoi(cur, sub, target, num-1)
        answer.append([cur, target])
        hanoi(sub, target, cur, num-1)

    answer = []
    hanoi(1, 3, 2, n)
    return answer

print(solution(3))