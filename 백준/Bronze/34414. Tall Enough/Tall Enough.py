def find(a):
    for i in range(a):
        b = int(input())
        if b < 48:
            return False
    return True
a = int(input())
print(find(a))