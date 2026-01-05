import sys
input = sys.stdin.readline
from collections import Counter
a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))
b = Counter(b)
for i in d:
    print(b[i],end=" ")