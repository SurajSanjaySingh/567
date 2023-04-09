x, y = 0, 0
for _ in range(int(input())):
  d, m = input().split()
  m = int(m)
  if d == "север":
    y += m
  elif d == "юг":
    y -= m
  elif d == "восток":
    x += m
  elif d == "запад":
    x -= m
print(x, y)