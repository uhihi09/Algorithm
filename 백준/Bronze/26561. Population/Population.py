a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    ans = b-(c//7)+c//4
    print(ans)