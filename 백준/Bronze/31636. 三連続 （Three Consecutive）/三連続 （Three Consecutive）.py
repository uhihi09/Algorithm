a = int(input())
b = list(input())
ans = False
for i in range(2,len(b)):
    if b[i-2] == "o" and b[i-1] == "o" and b[i] == "o":
        ans = True
if ans:
    print("Yes")
else:
    print("No")