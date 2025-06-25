a,b = map(int,input().split())
a *= b
if a%24200 >= 0:
    print(a//24200+1)
else:
    print(a//24200)