a,b = map(float,input().split())
cnt = a/b
if cnt < 0.2:
    print("weak")
elif 0.2 <= cnt < 0.4:
    print("normal")
elif 0.4 <= cnt < 0.6:
    print("strong")
elif 0.6 <= cnt:
    print("very strong")