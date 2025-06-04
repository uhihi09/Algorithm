def love(a):
    if a <= 1:
        return 1
    else:
        return a * love(a-1)
a = int(input())
print(love(a)//604800)