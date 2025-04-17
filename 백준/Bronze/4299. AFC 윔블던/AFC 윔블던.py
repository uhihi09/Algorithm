x,y = map(int, input().split())
a = ((x+y)/2)
if x > y:
    b = ((x-y)/2)
    if a != int(a) or b != int(b) or a <= 0 or b <= 0:
        print(-1)
    else:
        print(max(int(a),int(b)),min(int(a),int(b)))
elif y > x:
    c = ((x-y)/2)
    if a != int(a) or c != int(c) or a <= 0 or c <= 0:
        print(-1)
    else:
        print(max(int(a),int(c)),min(int(a),int(c)))
elif x == 0 and y == 0:
    print(0,0)
else:
    print(-1)