def convert(k,num):
    temp = []
    val = num

    while val > 1:
        mod = val % k
        print(mod)
        s = val // k
        val = s
        temp.append(mod)
    temp.append(val)
    temp.reverse()
    return temp


print(convert(2,10))
# print(10 % 1)