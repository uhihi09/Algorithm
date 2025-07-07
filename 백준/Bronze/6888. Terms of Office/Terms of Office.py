a = int(input())
b = int(input())
cnt = a
for i in range(a,b+1):
    if cnt > b:
        break
    else:
        print(f"All positions change in year {cnt}")
        cnt += 60