W, H, x, y, r = map(int, input().split())
if x >= r and W >= x + r and y >= r and H >= y + r :
    print('Yes')
else :
  print('No')
