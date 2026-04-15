a = int(input())
cnt = {}
for i in range(a):
    var = input()
    cnt[var] = cnt.get(var, 0) + 1
many = (0,0)
for key in sorted(cnt.keys()):
    if cnt[key] > many[1]:
        many = (key,cnt[key])
print(many[0])