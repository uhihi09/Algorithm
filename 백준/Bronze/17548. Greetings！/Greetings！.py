a = list(input())
a.remove("h")
a.remove("y")
b = a.count("e")
for i in range(b):
    a.append("e")
a.append("y")
a.insert(0,"h")
print(*a,sep="")