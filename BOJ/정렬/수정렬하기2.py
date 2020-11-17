# 퀵정렬 시간초과
# 퀵정렬의 최악의 경우로 인해 시간초과가 발생했다
# 병합정렬의 경우 최악의 경우도 nlogn이므로 병합정렬을 이용하면 풀릴 것으로 예상
# 파이썬의 소트는 통과

# def partition(arr, start, end):
#     p = arr[end]
#     idx = start - 1
#
#     for j in range(start,end):
#         if arr[j] < p:
#             idx += 1
#             arr[idx], arr[j] = arr[j], arr[idx]
#     arr[idx+1], arr[end] = arr[end], arr[idx+1]
#     return idx + 1
#
#
# def quick_sort(arr, l, r):
#     if l < r:
#         pivot = partition(arr, l, r)
#         quick_sort(arr, 0, pivot-1)
#         quick_sort(arr, pivot+1, r)

def merge_sort(arr, l, r):
    pass


N = int(input())
answer = []
for _ in range(N):
    answer.append(int(input()))
merge_sort(answer, 0, len(answer)-1)
for num in answer:
    print(num)