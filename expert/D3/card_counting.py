# 영준이의 카드 카운팅 # 10:18
import sys
sys.stdin = open("card_counting.text","r")

t = int(input())

for test_case in range(1,t+1):
    card_dic={'S':13, 'D':13, 'H':13, 'C':13}
    card = input()
    card_list = []
    card_list += card
    n = len(card_list)
    card_added = []
    IsError = True
    for i in range(n-2):
        if i % 3 == 0:
            temp_ch  = card_list[i]
            card_str = card_list[i]+card_list[i+1]+card_list[i+2]
            if card_str not in card_added:
                card_dic[temp_ch] -= 1
                card_added.append(card_str)
            else:
                print('#{} ERROR'.format(test_case))
                IsError = False
                break
    if IsError == True:
        print('#{}'.format(test_case), end=' ')
        for val in card_dic.values():
            print(val, end=" ")
        print()
#12:00