Code 1:
a=input()
b=input()
s=input()
x=input()

for i in range(len(s)):
    for j in range(len(a)):
        if s[i]==a[j]:
            print(s[i].replace(a[j],b[j]),end='')
print('')

for i in range(len(x)):
    for j in range(len(b)):
        if x[i]==b[j]:
            print(x[i].replace(b[j],a[j]),end='')

Refactored Code:

a = input()
b = input()
s = input()
x = input()

for char in s:
    if char in a:
        idx = a.index(char)
        print(b[idx], end="")
    else:
        print(char, end="")
print()

for char in x:
    if char in b:
        idx = b.index(char)
        print(a[idx], end="")
    else:
        print(char, end="")
print()


Code 2:
a={}
d=int(input())
for i in range(d):
    a[input().lower()]=1
l=int(input())
for i in range(l):
    s=input().lower().split()
    for j in range(len(s)):
        if s[j] not in a:
            a[s[j]]=0
for i in a:
    if a[i]==0:
        print(i)

Refactored Code:

word_freq = {}
d = int(input())

for i in range(d):
    word_freq[input().lower()] = 1

l = int(input())

for i in range(l):
    sentence = input().lower().split()
    for word in sentence:
        if word not in word_freq:
            word_freq[word] = 0
            
for word in word_freq:
    if word_freq[word] == 0:
        print(word)