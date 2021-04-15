def check_chage(depth, remainder, cnt, answer):
    if depth == C:
        return cnt
    else:
        coin = coins[depth]
        best_cnt = remainder // coin
        ans = check_chage(depth + 1, remainder - (coin * best_cnt), cnt + best_cnt, answer)
        if ans: return ans

PRICE = 1000
amount_of_payment = int(input())
coins = [500, 100, 50, 10, 5, 1]
C = len(coins)
answer = check_chage(0, PRICE - amount_of_payment, 0, 0)
print(answer)
