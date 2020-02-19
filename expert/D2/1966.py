# 숫자를 정렬하자 # 16:21

def bubble_sorting(number, num):
    number_list = []
    number_list = number[:]
    for i in range(num-1,0,-1):
        for j in range(i):
            if number_list[j]>number_list[j+1]:
                number_list[j],number_list[j+1] = number_list[j+1],number_list[j]
    return number_list


t = int(input())
for test_case in range(1,t+1):
    n=int(input())
    num_str = list(map(int,input().split()))

    num_list = bubble_sorting(num_str,n)
    # print(f'#{test_case} {num_list}') # f-string에선 리스트 언팩하면서 출력이 적용되지 않음
    print(f'#{test_case}',end= ' ')
    print(*num_list)

# 16:42