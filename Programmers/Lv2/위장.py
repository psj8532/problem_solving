# 18:14 ~ 19:30
def solution(clothes):
    answer = 1
    parts = {}
    for cl, part in clothes:
        if part in parts:
            parts[part].append(cl)
        else:
            parts[part] = [cl]
    for k in parts:
        answer *= (len(parts[k])+1)

    return answer - 1

ex1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	# 5
ex2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	# 3
ex3 = []
for i in range(30):
    ex3.append([1,i])
print(solution(ex3))