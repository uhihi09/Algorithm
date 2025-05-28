a = int(input())
b = list(map(int,input().split()))
ans = sum(b)+((len(b)-1)*8)
print(ans//24,ans%24)