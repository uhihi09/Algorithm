a = list(input())
b = 0
c = ['M','O','B','I','S']
for i in c:
    if i in a:
        b+=1
if b == 5:
    print("YES")
else:
    print("NO")