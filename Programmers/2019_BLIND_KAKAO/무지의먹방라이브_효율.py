def solution(food_times, k):
    answer = 0
    foods = []
    for i in range(len(food_times)):
        foods.append([food_times[i], i])
    foods.sort(key=lambda x:x[0])
    total = 0
    mv = 0
    for i in range(len(foods)):
        mv = foods[i][0]
        if mv * (len(foods)-i) >= k-total:
            answer = (len(foods)-i) % (k-total) + 1


    return answer

ex1 = [[3,1,2], 5]
print(solution(*ex1))