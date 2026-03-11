a = int(input())
cnt = []
for i in range(a):
    cnt.append(input())
cnt = list(set(cnt))
cnt.sort(key=lambda x : (len(x),x))
for i in cnt:
    print(i)