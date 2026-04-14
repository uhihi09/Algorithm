import collections
def solve(command,array,list_len):
    if list_len == 0:
        return "error"
    front = True
    for ii in range(len(command)):
        if command[ii] == "R":
            front = not front
        elif command[ii] == "D":
            if len(array) == 0:
                return "error"
            else:
                if front:
                    array.popleft()
                else:
                    array.pop()
    if front:
        return '[' + ','.join(map(str,list(array))) + ']'
    array.reverse()
    return '[' + ','.join(map(str,list(array))) + ']'

a = int(input())
for i in range(a):
    command = list(input())
    list_len = int(input())
    if list_len == 0:
        var = input()
        if "D" in command:
            print("error")
        else:
            print(list())
    else:
        array = collections.deque(map(int,input()[1:-1].split(',')))
        print(solve(command,array,list_len))