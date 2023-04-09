n = int(input())
cl = {}
for i in range(n):
    st = input().split()
    if len(st) == 1:
        cl[st[0]] = []
    else:
        if st[0] not in cl:
            cl[st[0]] = [st[k] for k in range(2, len(st))]
        else:
            cl[st[0]] += [st[k] for k in range(2, len(st))]

for i in cl:
    for j in cl[i].copy():
        if j in cl:
            cl[i] += cl[j]

n = int(input())
for i in range(n):
    st = input().split()
    if st[0] == st[1] or st[0] in cl.get(st[1], []):
        print('Yes')
    else:
        print('No')