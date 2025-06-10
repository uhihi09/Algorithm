a,b = map(int,input().split())
c = 100-a
d = 100-b
e = 100-(c+d)
f = c*d
g = f//100
h = f%100
print(c,d,e,f,g,h)
print(e+g,h)