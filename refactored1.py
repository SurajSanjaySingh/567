n = int(input())
a = [[0] * n for i in range(n)]
k, x, y = 1, 0, n
while k <= n*n:
    for j in range(x, y):
        a[x][j] = k
        k += 1
    x += 1
    for i in range(x, y):
        a[i][y-1] = k
        k += 1
    y -= 1
    for j in range(y-1, x-1, -1):
        a[y-1][j] = k
        k += 1
    for i in range(y-2, x-1, -1):
        a[i][x-1] = k
        k += 1
    x += 1
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))