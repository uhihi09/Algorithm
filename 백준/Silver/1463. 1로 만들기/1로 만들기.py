import collections
a = int(input())
q = collections.deque()
q.append((a,0))
visited = set()
while q:
    num,cnt = q.popleft()
    if num in visited:
        continue
    visited.add(num)
    if num == 1:
        print(cnt)
        break
    if num % 3 == 0:
        q.append((num//3, cnt + 1))
    if num % 2 == 0:
        q.append((num//2, cnt + 1))
    q.append((num-1, cnt + 1))