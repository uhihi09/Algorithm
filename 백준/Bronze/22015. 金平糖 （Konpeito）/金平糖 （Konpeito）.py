a,b,c=  map(int,input().split())
cnt = [a,b,c]
cnt.remove(max(a,b,c))
cnt.remove(min(a,b,c))
print(max(a,b,c)-min(a,b,c)+max(a,b,c)-cnt[0])