def partition(arr,start,end):
    p = arr[end]
    i = start - 1 # pivot보다 작은 원소들의 마지막 위치

    for j in range(start,end):
        if arr[j] < p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1


def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr,l,r)
        quick_sort(arr,l,pivot-1)
        quick_sort(arr,pivot+1,r)


N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))
quick_sort(a, 0, N-1)
for num in a:
    print(num)