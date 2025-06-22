def pac(a):
    result = 1
    for i in range(2, a+1):
        result *= i
    return result
cnt = str(pac(int(input())))
print(cnt[-1])