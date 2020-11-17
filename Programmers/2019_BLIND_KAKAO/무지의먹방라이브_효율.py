def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k: return -1
    foods = []
    for idx,val in enumerate(food_times):
        foods.append([val,idx+1])
    foods.sort(key=lambda x:x[0])
    total = cnt = min_val = 0
    for i, data in enumerate(foods):
        val, idx = data
        cur, remain = val - cnt, len(foods)-i
        if min_val == val: continue
        if cur * remain > k - total:
            remain_lst = foods[i:]
            remain_lst.sort(key = lambda x:x[1])
            return remain_lst[(k-total) % remain][1]
        else:
            total += cur * remain
            cnt += cur
            min_val = val

    return answer

ex1 = [[3,1,2], 5]
ex2 = [[10,10,50,50,55], 168]
ex3 = [[5,10,5], 14]
ex4 = [[7,8,3,3,2,2,2,2,2,2,2,2], 35]
ex5 = [[3,1,1,1,2,4,3], 12]
ex6 = [[4,3,5,6,2], 7]
ex7 = [[4,1,1,5], 4]
ex8 = [[4,2,3],5]
print(solution(*ex6))