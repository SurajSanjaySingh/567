b = {}
n = int(input())

for i in range(n):
    a = input().split(';')
    
    b.setdefault(a[0], {'game':0,'win':0,'draw':0,'defeat':0,'point':0})
    b.setdefault(a[2], {'game':0,'win':0,'draw':0,'defeat':0,'point':0})
    
    if int(a[1]) < int(a[3]):
        b[a[0]]['game'] += 1
        b[a[0]]['defeat'] += 1
        b[a[2]]['game'] += 1
        b[a[2]]['win'] += 1
        b[a[2]]['point'] += 3
    elif int(a[1]) > int(a[3]):
        b[a[0]]['game'] += 1
        b[a[0]]['win'] += 1
        b[a[0]]['point'] += 3
        b[a[2]]['game'] += 1
        b[a[2]]['defeat'] += 1
    else:
        b[a[0]]['game'] += 1
        b[a[0]]['draw'] += 1
        b[a[0]]['point'] += 1
        b[a[2]]['game'] += 1
        b[a[2]]['draw'] += 1
        b[a[2]]['point'] += 1

for key in b.keys():
    print(key, end=':')
    print(b[key]['game'], b[key]['win'], b[key]['draw'], b[key]['defeat'], b[key]['point'], sep=' ')