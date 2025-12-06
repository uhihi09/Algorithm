import math
a,b,c = map(int,input().split())
cnt = (c-b) / (a-b)
print(math.ceil(cnt))