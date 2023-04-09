word_dict = {}
d = int(input())

for i in range(d):
    word_dict[input().lower()] = 1

l = int(input())

for i in range(l):
    words = input().lower().split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0

for word in word_dict:
    if word_dict[word] == 0:
        print(word)