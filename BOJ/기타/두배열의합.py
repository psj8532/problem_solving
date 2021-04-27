T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

def get_sublist(lst, size):
    sum_dict = {}
    for k in range(size):
        for i in range(size - k):
            sum_val = 0
            for j in range(i, i + k + 1):
                sum_val += lst[j]
            if sum_val in sum_dict: sum_dict[sum_val] += 1
            else: sum_dict[sum_val] = 1
    return sum_dict

a_sublist = get_sublist(A, N)
b_sublist = get_sublist(B, M)
answer = 0
for a, cnt in a_sublist.items():
    b = T - a
    if b in b_sublist: answer += cnt * b_sublist[b]
print(answer)
