i=0
b=[]
while True:
    e=input().split()
    if 'end' in e:
        break
    else:
        a=[int(j) for j in e]
        b.append(a)
c=[]
for i in range(len(b)):
    for j in range(len(b[i])):
        c.append(b[i-1][j]+b[(i+1)%len(b)][j]+b[i][j-1]+b[i][(j+1)%len(b[i])])
for i in range(len(c)):
    print(c[i], end=' ')
    if (i+1)%len(b[0])==0:
        print('')