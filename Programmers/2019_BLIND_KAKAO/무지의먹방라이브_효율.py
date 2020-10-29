def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k: return -1
    foods = []
    for idx,val in enumerate(food_times):
        foods.append([val,idx+1])
    foods.sort(key=lambda x:x[0])
    total = cnt = min_val = 0
    for i in range(len(foods)):
        cur_val = foods[i][0]
        if min_val == cur_val: continue
        if (cur_val-cnt) * (len(foods)-i) > k - total:
            answer = foods[i + ((k-total) % (len(foods)-i))][1]
        else:
            total += (cur_val-cnt) * (len(foods)-i)
            cnt += (cur_val-cnt)
            min_val = cur_val

    return answer

ex1 = [[3,1,2], 5]
print(solution(*ex1))