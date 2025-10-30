cnt = "UAPC"
a = input()
ans = ""
for i in cnt:
    if i not in a:
        ans += i
print(ans)