a = int(input())
for i in range(a):
    b,c,d = map(int, input().split())
    rooms = []
    for ii in range(1,b+1):
        row = []
        for iii in range(1,c+1):
            row.append(100*ii+iii)
        rooms.append(row)
    print(rooms[(d-1)%b][(d-1)//b])