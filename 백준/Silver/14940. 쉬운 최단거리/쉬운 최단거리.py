import sys
import collections
input = sys.stdin.readline
def isValid(x,y):
    if 0 <= y < n and 0 <= x < m:
        if not visited[y][x] and maze[y][x] == 1:
            return True
    return False
n,m = map(int,input().split())
maze = []
visited = [[False for j in range(m)] for i in range(n)]
queue = collections.deque()
for i in range(n):
    var = list(map(int,input().strip().split()))
    maze.append(var)
    if 2 in var:
        start = var.index(2), i
        queue.append(start)
        maze[start[1]][start[0]] = 0
while len(queue) != 0:
    here = queue.popleft()
    x,y = here
    visited[y][x] = True
    if isValid(x,y-1):
        queue.append((x,y-1))
        maze[y-1][x] = maze[y][x] + 1
    if isValid(x,y+1):
        queue.append((x,y+1))
        maze[y+1][x] = maze[y][x] + 1
    if isValid(x-1,y):
        queue.append((x-1,y))
        maze[y][x-1] = maze[y][x] + 1
    if isValid(x+1,y):
        queue.append((x+1,y))
        maze[y][x+1] = maze[y][x] + 1
for i in range(len(maze)):
    for j in range(len(maze[i])):
            if maze[i][j] == 1 and visited[i][j] == False:
                maze[i][j] = -1
for i in maze:
    print(*i)