# 종이 자르기 # 16:43
import sys
sys.stdin=open("2628.text","r")

#이중 for문으로 범위를 이용하여 면적 계산후 리스트에 저장, 그 중 큰 값을 뽑아냄
w,h = map(int,input().split())
cut = int(input())
hcut_list = [0]
wcut_list = [0]
#정보를 입력받아서 몇 번이 잘리는지 저장
for idx in range(cut):
    cut_list = list(map(int,input().split()))
    #cut_list[0]:w_cut, h_cut
    #cut_list[1]:cut_num
    if cut_list[0]:
        hcut_list.append(cut_list[1])
    else:
        wcut_list.append(cut_list[1])
hcut_list.sort() #세로 정보
wcut_list.sort() #가로 정보
hcut_list.append(w) #세로리스트 마지막에 가로의 끝부분을 넣어줌
wcut_list.append(h)

area_list = []
# 리스트의 각 인덱스 번호까지의 길이를 잘라서 곱하면 면적나옴
# area = hcut_list[]*wcut_list[]
# 뒤에서부터 면적 구해서 빼는게 나음
for i in range(1,len(hcut_list)): #가로확장
        for j in range(1,len(wcut_list)): #세로 확장
                area = (wcut_list[j]-wcut_list[j-1])*(hcut_list[i]-hcut_list[i-1])         
                area_list.append(area)
print(max(area_list))
# 18:53