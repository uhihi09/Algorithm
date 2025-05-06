import sys

input = sys.stdin.readline
a = int(input())
b = [0] * 10001
for i in range(a):
    c = int(input())
    b[c] += 1
for i in range(1,10001):
    for ii in range(b[i]):
        print(i)