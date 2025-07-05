a = int(input())
b = int(input())
if b > a:
    print(a*1500)
elif a-60-b < 0:
    print(a*1500)
elif a-b <= 60:
    print(a*1500)
elif a-b > 60:
    print((60+b)*1500+(a-60-b)*3000)