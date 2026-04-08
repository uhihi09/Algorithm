def solve(a):
    arr = [0] * (a+3)
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    if a == 1 or a == 2 or a == 3:
        return a
    for i in range(2,a+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[a-1]
print(solve(int(input()))%10007)