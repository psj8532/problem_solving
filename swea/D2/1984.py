#중간 평균값 구하기
t = int(input())

for test_case in range(1,t+1):
    num_list = list(map(int, input().split()))
    result = 0
    n=len(num_list)
    exit=1 # 제약 사항에 걸릴 경우 프로그램 종료용 변수
    for i in range(n):
        if 0<=num_list[i]<=10000: # 제약 사항
            continue           
        else:
            exit=0
    if exit:
        num_list.sort()
        for i in range(1, n-1):
            result += num_list[i]

        ave = int(round((result/(n-2)),0))

        print(f'#{test_case} {ave}')