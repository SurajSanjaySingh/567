s = input()
t = input()
k = 0
for i in range(len(s)):
    if t in s and s.startswith(t):
        k += 1
    s = s[1:]
print(k)