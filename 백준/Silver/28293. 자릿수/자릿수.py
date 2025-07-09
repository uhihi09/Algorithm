import sys
import math
input = sys.stdin.readline
a,b = map(int,input().split())
ans = math.log10(a) * b
ans = int(ans)
print(ans+1)