s=int(input())
h=s//3600
m=h%3600//60
s=s%60
print(f'{h}:{m}:{s}')
