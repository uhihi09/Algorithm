import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    stack = []
    b = list(input().strip())
    # print(len(b))
    cnt = True
    for ii in b:
        if ii == "(":
            stack.append(ii)
            # print(stack)
        else:
            if len(stack) == 0:
                cnt = False
                # print(stack)
            else:
                stack.pop()
                # print(stack)
    if cnt and len(stack) == 0:
        print("YES")
    else:
        print("NO")