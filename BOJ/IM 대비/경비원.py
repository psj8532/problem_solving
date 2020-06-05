# 경비원    # 14:09
w, h = map(int,input().split())
num = int(input())
data_y = []
data_x = []
for i in range(num+1):
    data = list(map(int,input().split()))
    
    if i!=num:
        if data[0] == 1:
            data_y.append(0)
            data_x.append(data[1])
        elif data[0] == 2:
            data_y.append(h)
            data_x.append(data[1])
        elif data[0] == 3:
            data_y.append(data[1])
            data_x.append(0)
        else:
            data_y.append(data[1])
            data_x.append(w)
    else:
        if data[0] == 1:
            posi_y = 0
            posi_x = data[1]
        elif data[0] == 2:
            posi_y = h
            posi_x = data[1]
        elif data[0] == 3:
            posi_y = data[1]
            posi_x = 0
        else:
            posi_y = data[1]
            posi_x = w

# data_y[num]: 현재 위치
result = 0
for i in range(num):
    if posi_y == 0:
        if posi_y == data_y[i]:
            result += abs(data_x[i] - posi_x)
        else:
            if data_x[i] == 0:
                result = result + posi_x + data_y[i]
            elif data_x[i] == w:
                result = result + (w-posi_x) + data_y[i] 
            else:
                temp1=posi_x + h + data_x[i]
                temp2=(w-posi_x) + h + (w-data_x[i])
                if temp1 > temp2:
                    result+=temp2
                else:
                    result+=temp1
    elif posi_y == h:
        if posi_y == data_y[i]:
            result += abs(data_x[i] - posi_x)
        else:
            if data_x[i] == 0:
                result = result + posi_x + (h-data_y[i])
            elif data_x[i] == w:
                result = result + (w-posi_x) + (h-data_y[i]) 
            else:
                temp1=posi_x + h + data_x[i]
                temp2=(w-posi_x) + h + (w-data_x[i])
                if temp1 > temp2:
                    result+=temp2
                else:
                    result+=temp1
    elif posi_x == 0:
        if posi_x == data_x[i]:
            result += abs(data_y[i] - posi_y)
        else:
            if data_y[i] == 0:
                result = result + posi_y + data_x[i]
            elif data_y[i] == h:
                result = result + (h-posi_y) + data_y[i] 
            else:
                temp1=posi_y + w + data_y[i]
                temp2=(h-posi_y) + w + (h-data_y[i])
                if temp1 > temp2:
                    result+=temp2
                else:
                    result+=temp1
    elif posi_x == w:
        if posi_x == data_x[i]:
            result += abs(data_y[i] - posi_y)
        else:
            if data_y[i] == 0:
                result = result + posi_y + (w-data_x[i])
            elif data_y[i] == h:
                result = result + (h-posi_y) + (w-data_y[i]) 
            else:
                temp1=posi_y + w + data_y[i]
                temp2=(h-posi_y) + w + (h-data_y[i])
                if temp1 > temp2:
                    result+=temp2
                else:
                    result+=temp1
print(result)
#16:50