#17281 15:29 ~ 16:46 시간초과
from itertools import permutations

def on_base(hit, base, score):
    new_base = []
    for runner in base:
        next_base = runner + hit
        if next_base >= 4:
            score += 1
        else:
            new_base.append(next_base)
    new_base.append(hit)
    return new_base, score

N = int(input())
score_table = [list(map(int,input().split())) for _ in range(N)]
max_score = 0
perm = list(map(list,permutations(list(range(1,9)), 8)))
for i, order in enumerate(perm):
    order.insert(3, 0)
    score, innings, curr_batsman = 0, 0, 0
    while innings < N:
        base, out_count = [], 0
        while out_count < 3:
            batsman = order[curr_batsman]
            hits = score_table[innings][batsman]

            if not hits :
                out_count += 1
            elif hits == 4:
                score += len(base) + 1
                base = []
            else:
                base, score = on_base(hits, base, score)
            curr_batsman = (curr_batsman + 1) % 9
        innings += 1

    if score > max_score: max_score = score

print(max_score)