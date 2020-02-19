# 스위치 켜고 끄기 # 22:52
import sys
sys.stdin = open("1244.text","r")

switch = int(input()) #스위치 갯수
light = list(map(int,input().split())) #조명의 처음 상태
student = int(input()) #학생의 수

for i in range(student):
    data = list(map(int,input().split())) #성별과 부여받은 스위치 번호
    if data[0] == 1: #남자인 경우
        for j in range(1, switch+1):
            if j % data[1] == 0: #스위치 번호가 부여받은 번호의 배수이면
                #스위치 반전
                light[j-1] = 1 - light[j-1]                
    
    elif data[0] == 2: #여자인 경우 #부여받은 번호부터 좌우로 뻗어나가야함        
        light[data[1]-1] = 1 - light[data[1]-1]
        if data[1]==1 or data[1]==switch:
            continue
        for j in range(1,data[1]+1):
            if data[1]-j == 0 or data[1]+j == switch:
                break            
            if light[data[1]-1-j]==light[data[1]-1+j]:
                light[data[1]-1-j] = 1 - light[data[1]-1-j]
                light[data[1]-1+j] = 1 - light[data[1]-1-j]
            else:
                break

for i in range(switch):
    print(light[i], end=' ')
    if (i+1)%20 == 0:
        print()
                     
 # 11:25 중단 #15:06 재개 16:40 히든케이스 오류로 인한 중단
 # 21:11 다시 시작