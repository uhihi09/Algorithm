a = int(input())
b = list(input())
if b[-1] == "G":
    b.pop(-1)
else:
    b.append('G')
print(*b,sep="")