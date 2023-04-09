i,j=0,0
k=1
n=int(input())
a=[[0]*n for i in range(n)]
x,y=0,n
while k<=n*n:
  for j in range(x,y):
    a[i][j]=k
    k+=1
  x+=1
  for i in range(x,y):
    a[i][j]=k
    k+=1
  x-=1
  y-=1
  for j in range(y-1,x-1,-1):
    a[i][j]=k
    k+=1
  x+=1
  for i in range(y-1,x-1,-1):
    a[i][j]=k
    k+=1
for i in range(n):
  print(*a[i])