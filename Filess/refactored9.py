a = input()
b = input()
s = input()
x = input()

for char in s:
    if char in a:
        print(b[a.index(char)], end='')
    else:
        print(char, end='')
print()

for char in x:
    if char in b:
        print(a[b.index(char)], end='')
    else:
        print(char, end='')