import collections
import sys
input = sys.stdin.readline
a = int(input())
numbers = []
ins = collections.deque()
stack = collections.deque()
ans = []
ans1 = True
for i in range(1,a+1):
    numbers.append(i)
    ins.append(int(input()))
while True:
    if len(numbers) == 0:
        if len(stack) != 0 and ins[0] != stack[-1]:
            print("NO")
            ans1 = False
            break
        for i in range(len(stack)):
            ans.append("-")
        break
    if len(stack) != 0 and stack[-1] == ins[0]:
        ins.popleft()
        stack.pop()
        ans.append("-")
    elif ins[0] != numbers[0]:
        stack.append(numbers.pop(0))
        ans.append("+")
    elif ins[0] == numbers[0]:
        stack.append(numbers.pop(0))
        ans.append("+")
        stack.pop()
        ans.append("-")
        ins.popleft()
if ans1:
    for i in ans:
        print(i)