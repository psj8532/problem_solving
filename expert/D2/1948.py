# 날짜 계산기 # 7:17
import sys
sys.stdin=open("1948.text","r")
# 월별 일수 리스트 저장
t = int(input())

mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #인덱싱 할때 월-1이 인덱스 번호인 것에 유의

for test_case in range(1,t+1):
# 두개의 월 사이에 있는 일수 다 더하고, 해당 월에서 말일과 초일부터의 일수 계산
    date = list(map(int,input().split())) # date[0],date[2]: 월  #date[1],date[3]: 일
    day = 0
    if date[0] != date[2]:
        for i in range(date[0]+1,date[2]):                       
            day+=mon[i-1]
        day = day+(mon[date[0]-1]-date[1]+1)
        day += date[3]
    elif date[0]==date[2]:
        day = date[3]-date[1]+1
    print(f'#{test_case} {day}')