def solution(prices):
    l = len(prices)
    answer = [l-i-1 for i in range(len(prices))]
    cand_keys = []
    cand_idx = {}

    def upper_bound(s, e, p):
        if s >= e:
            return s
        mid = (s + e) // 2
        if cand_keys[mid] <= p:
            return upper_bound(mid + 1, e, p)
        else:
            return upper_bound(s, mid, p)

    for idx, price in enumerate(prices):
        if cand_keys and cand_keys[-1] > price:
            # 이분 탐색
            target = upper_bound(0,len(cand_keys)-1,price)
            for i in range(len(cand_keys)-1,target-1,-1):
                key = cand_keys[i]
                for j in cand_idx[key]:
                    diff = idx - j
                    answer[j] = diff
                del cand_idx[key]
                cand_keys.pop()
        if price in cand_idx:
            cand_idx[price].append(idx)
        else:
            cand_keys.append(price)
            cand_idx[price] = [idx]

    return answer

# prices	return
ex1 = [1, 2, 3, 2, 3] # [4, 3, 1, 1, 0]
ex2 = [5, 4, 3, 2, 1]
print(solution(ex2)) # [1, 1, 1, 1, 0]