class LoggableList(list, Loggable):
    def append(self, x):
        super().append(x)
        self.log(x)

x = int(input())
cl = {}

for i in range(x):
    st = input().split()
    if len(st) == 1:
        cl[st[0]] = []
    else:
        cl.setdefault(st[0], []).extend(st[2:])

for i in cl:
    for j in cl[i]:
        if j in cl:
            cl[i] += cl[j]

x = int(input())
st = []
st1 = []

for i in range(x):
    st.append(input())

for j in range(len(st)):
    for i in range(j):
        if st[i] in cl[st[j]]:
            st1.append(st[j])
            break

for i in st1:
    print(i)