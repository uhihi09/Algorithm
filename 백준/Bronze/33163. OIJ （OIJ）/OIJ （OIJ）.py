a = int(input())
b = list(input())
ans = ""
for i in b:
    if i == "J":
        ans += "O"
    elif i == "O":
        ans += "I"
    elif i == "I":
        ans += "J"
print(ans)