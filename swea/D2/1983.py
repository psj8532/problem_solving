# 조교의 성적 매기기
import sys
sys.stdin = open("1983.text","r")

t=int(input())

for test_case in range(1,t+1):
    n, k = map(int,input().split())
    people_score = []
    people_dsc=[]
    for people in range(n):
        score_temp = list(map(int,input().split()))
        score = score_temp[0]*0.35 +score_temp[1]*0.45 + score_temp[2]*0.2
        people_score.append(score) #k번째 학생의 점수는 people_score[k-1]에 저장되어있음
    result = people_score[k-1] # 오름차순 정렬했을 때 k 학생의 점수 찾기 용도
    people_score.sort()
    people_dsc = people_score[::-1]
    for i in range(n):
        if result==people_dsc[i]:
            position = i+1 # k 학생의 등수
    if position <= (n//10):
        grade = 'A+'
    elif position<=(n//10)*2:
        grade = 'A0'
    elif position<=(n//10)*3:
        grade = 'A-'
    elif position<=(n//10)*4:
        grade = 'B+'
    elif position<=(n//10)*5:
        grade = 'B0'
    elif position<=(n//10)*6:
        grade = 'B-'
    elif position<=(n//10)*7:
        grade = 'C+'  
    elif position<=(n//10)*8:
        grade = 'C0'
    elif position<=(n//10)*9:
        grade = 'C-'
    else:
        grade = 'D0'
    print(f'#{test_case} {grade}')