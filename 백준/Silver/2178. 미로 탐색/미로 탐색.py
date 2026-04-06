import sys
import collections
input = sys.stdin.readline
def isvalid(x,y):
    if y < n and x < m:
        if y >= 0 and x >= 0:
            if maze[y][x] == 1:
                return True
    return False
n,m = map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input().strip())))
queue = collections.deque()
queue.append((0,0))
# [y][x]
while len(queue) != 0:
    here = queue.popleft()
    x,y = here
    if x == m-1 and y == n-1:
        break
    if isvalid(x,y-1):
        queue.append((x,y-1))
        maze[y-1][x] += maze[y][x]
    if isvalid(x,y+1):
        queue.append((x,y+1))
        maze[y+1][x] += maze[y][x]
    if isvalid(x-1,y):
        queue.append((x-1,y))
        maze[y][x-1] += maze[y][x]
    if isvalid(x+1,y):
        queue.append((x+1,y))
        maze[y][x+1] += maze[y][x]
print(maze[n-1][m-1])