p,q = map(int, input().split())
a,b = map(int, input().split())
if p<q:
    print(p*a+(q-p)*b)
else:
    print(q*a)