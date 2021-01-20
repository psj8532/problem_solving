# 20:48 ~ 23:03
from _collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    position = [0] * len(truck_weights)
    bridge = deque()
    end = -1
    bridge_w = 0
    for idx, truck_w in enumerate(truck_weights):
        wait = False
        while truck_w + bridge_w > weight:
            lead = bridge.pop()
            dist = bridge_length-position[lead]+1
            for i in range(end+1,idx):
                position[i] += dist
            position[lead] = -1
            end = lead
            bridge_w -= truck_weights[lead]
            answer += dist
            wait = True

        if not wait:
            answer += 1
            if position[end + 1] == bridge_length:
                lead = bridge.pop()
                position[end + 1] = -1
                end += 1
                bridge_w -= truck_weights[lead]
            for i in range(end + 1, idx):
                position[i] += 1
        position[idx] = 1
        bridge.appendleft(idx)
        bridge_w += truck_w
        # 새로운 트럭이 다리에 완전히 들어옴
    if bridge:
        rear = bridge.popleft()
        answer += bridge_length-position[rear]+1

    return answer

# bridge_length	weight	truck_weights	return
ex1 = [2, 10, [7,4,5,6]] # 8
ex2 = [100, 100, [10]] # 101
ex3 = [100,	100, [10,10,10,10,10,10,10,10,10,10]] # 110
ex4 = [5, 10, [5,5,10,10]] # 17
ex5 = [5, 10, [10,10,10]] # 16
ex6 = [5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]] # 19
print(solution(*ex4))