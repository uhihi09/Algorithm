a = int(input())
b = input()
if a%2==0:
    cnt = a//2
else:
    cnt = a//2+1
if b.count("O") >= cnt:
    print("Yes")
else:
    print("No")