#summation #21:15
import sys
sys.stdin = open("8658.text","r")

def data_list(a):
    num_list = []

    for i in range(len(a)):
        num = a[i]
        count = 0

        while num!=0:
            num //= 10
            count += 1
        
        b = [0]*count
        num = a[i]
        
        for j in range(count-1,-1,-1):
            b[j] = num % 10
            num //= 10

        num_list.append(b)

    return num_list    

def data_sum(a):
    data_temp = []
    for i in range(10):
        sum_val = 0
        for j in range(len(a[i])):
            sum_val += a[i][j]
        data_temp.append(sum_val)
            
    max_val = max(data_temp)
    min_val = min(data_temp)

    return max_val, min_val


t = int(input())

for test_case in range(1, t+1):
    data = list(map(int,input().split()))

    new_data = data_list(data)
    max_value, min_value = data_sum(new_data)
    print('#{} {} {}'.format(test_case, max_value, min_value))

# 21:42