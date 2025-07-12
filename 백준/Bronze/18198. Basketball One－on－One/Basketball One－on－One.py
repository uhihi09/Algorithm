a = list(input())
cnt1 = 0
cnt2 = 0
for i in range(0,len(a),2):
    if a[i] == "A":
        cnt1 += int(a[i+1])
    elif a[i] == "B":
        cnt2 += int(a[i+1])
    if cnt1 >= 11 or cnt2 >= 11:
        if abs(cnt1 - cnt2) >= 2:
            if cnt1 >= cnt2:
                print('A')
            else:
                print('B')