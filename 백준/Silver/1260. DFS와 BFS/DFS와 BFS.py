import sys
import collections
input = sys.stdin.readline
n,m,v = map(int,input().strip().split())
stack, queue = collections.deque(), collections.deque()
stack_visited, queue_visited = set(), set()
edge = {}
ans1, ans2 = [], []
for i in range(m):
    a,b = map(int,input().split())
    if a not in edge.keys():
        edge[a] = []
    edge[a].append(b)
    if b not in edge.keys():
        edge[b] = []
    edge[b].append(a)
stack.append(v)
queue.append(v)
while stack:
    num = stack.pop()
    var1 = edge.get(num, [])
    if num in stack_visited:
        continue
    stack_visited.add(num)
    ans1.append(num)
    var1.sort(reverse=True)
    for i in var1:
        stack.append(i)
print(*ans1)
num = 0
var2 = 0
while queue:
    num = queue.popleft()
    var2 = edge.get(num, [])
    if num in queue_visited:
        continue
    queue_visited.add(num)
    ans2.append(num)
    var2.sort()
    for i in var2:
        queue.append(i)
print(*ans2)