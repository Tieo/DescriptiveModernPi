def solution(v):
    answer = []
    a = []
    x = []
    y = []
    
    for i in v:
        for j in i:
            a.append(j)
    for k in range(0,5,2):
        if a[k] not in x:
            x.append(a[k])
        else:
            x.remove(a[k])
    for k in range(1,6,2):
        if a[k] not in y:
            y.append(a[k])
        else:
            y.remove(a[k])
            
    answer.append(x[0])
    answer.append(y[0])
    
    return answer