# 일곱 난장이 # 20:30
import sys
sys.stdin = open("2309.text","r")

# def bubble_sorting(a):
#     n = len(a)
#     for i in range(n-1,0,-1):
#         for j in range(0,i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# def selection_sorting(a):
#     n=len(a)
#     for now in range(n-1):
#         min_val = a[now]
#         posi = now
#         for i in range(now, n):
#             if min_val > a[i]:
#                 posi = i
#                 min_val = a[i]
#         a[now], a[posi] = a[posi], a[now]
#     return a

people = []
for i in range(9):
    people.append(int(input()))

sum_val=0
for i in range(9):
    sum_val += people[i]
diff = sum_val - 100

# temp_people = people[:]

# for i in range(8):
#     for j in range(i+1,9):
#         if diff == people[i]+people[j]:
#             temp_people.remove(people[i])
#             temp_people.remove(people[j])
#             break

# temp_people = people[:]
IsEnd = False
for i in range(8):
    for j in range(i+1,9):
        if diff == people[i]+people[j]:
            people[i] = 0
            people[j] = 0
            IsEnd =True
            break
    if IsEnd ==True:
        break
# temp_people = selection_sorting(temp_people)
people.sort()
for i in range(2,9):
    print(people[i])