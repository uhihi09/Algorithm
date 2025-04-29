a,b,c = map(int, input().split())
if a+b+c >= 100:
    print("OK")
else:
    if a<b<c or a<c<b :
        print("Soongsil")
    elif b<a<c or b<c<a:
        print("Korea")
    else:
        print("Hanyang")