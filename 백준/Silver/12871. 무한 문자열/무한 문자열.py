def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a = input()
b = input()
lcm = (len(a)*len(b))//gcd(len(a),len(b))
ans1 = a*(lcm//len(a))
ans2 =b*(lcm//len(b))
if ans1 == ans2:
    print(1)
else:
    print(0)