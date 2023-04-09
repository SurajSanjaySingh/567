def modify_list(l):
  i = 0
  while i < len(l):
    if l[i] % 2 == 0:
      l[i] //= 2
      i += 1
    else:
      del l[i]
  return l