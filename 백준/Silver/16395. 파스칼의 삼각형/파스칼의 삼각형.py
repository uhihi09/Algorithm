a,b = map(int,input().split())
tri = []
for i in range(a):
    row = [1] * (i+1)
    for ii in range(1,i):
        row[ii] = tri[i-1][ii]+tri[i-1][ii-1]
    tri.append(row)
print(tri[a-1][b-1])