import sys
input = sys.stdin.readline
a = input()
cnt = {"a":"4","e":"3","i":"1","o":"0","s":"5"}
for i in cnt:
    if i in a:
        a = a.replace(i,cnt[i])
print(a)