a = input()
cnt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in cnt:
    if i not in a:
        print(i)
        break