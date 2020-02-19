def counting_sort(a,b,k):
    c = [0]*(k+1)

    for i in range(len(a)):
        c[a[i]]+=1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in range(len(b)-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
    return b

a = [1,6,8,4,2,3,5,3,7,5]

b = a[:]

print(counting_sort(a,b,max(a)))