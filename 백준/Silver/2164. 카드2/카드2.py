import sys
input = sys.stdin.readline
import queue
a = int(input())
cnt = queue.Queue()
for i in range(1,a+1):
    cnt.put(i)
while True:
    if cnt.qsize() == 1:
        print(cnt.get())
        break
    cnt.get()
    cnt.put(cnt.get())