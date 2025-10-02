import sys
input = sys.stdin.readline

a = int(input())
for i in range(1,a+1):
    b = list(map(int,input().split()))
    c = b[0]
    b.pop(0)
    b.sort(reverse=True)
    cnt = 0
    for ii in range(1,len(b)):
        if abs(b[ii-1]-b[ii]) >= cnt:
            cnt = abs(b[ii-1]-b[ii])
    print(f"Class {i}")
    print(f"Max {max(b)}, Min {min(b)}, Largest gap {cnt}")