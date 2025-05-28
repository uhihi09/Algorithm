a = int(input())
b = input()
ans = []
for i in b:
    if i.isupper() == True:
        ans.append(i.lower())
    else:
        ans.append(i.upper())
print(*ans,sep="")