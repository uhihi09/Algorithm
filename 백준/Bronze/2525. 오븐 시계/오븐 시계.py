h,m = map(int,input().split())
a = int(input())
b = (m+a)//60
c = a%60
h += b
m += c
if m >= 60:
  m -= 60
  if h >=24:
    h -=24
    print(h,m)
  elif h < 24:
    print(h,m)
elif m <60:
  if h >=24:
    h -= 24
    print(h,m)
  elif h < 24:
    print(h,m)