a = int(input())
b = list(input())
cnt = []
for i in range(len(b)-1):
    if b[i+1] == "J":
        print(b[i])