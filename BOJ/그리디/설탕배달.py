def check(idx, remainder, cnt):
    global answer
    if idx == 2:
        if not remainder:
            answer = cnt
            return True
    else:
        i = 0
        best_fit = remainder // sugar_list[idx]
        for fit in range(best_fit, -1, -1):
            if check(idx + 1, remainder - (sugar_list[idx] * fit), cnt + fit): return True
    return False

N = int(input())
sugar_list = [5, 3]
answer = -1
check(0, N, 0)
print(answer)