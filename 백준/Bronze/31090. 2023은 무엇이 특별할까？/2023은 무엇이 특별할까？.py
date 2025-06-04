a = int(input())
for i in range(a):
    b = input()
    if (int(b)+1)%(int(b[2:4])) == 0:
        print("Good")
    else:
        print("Bye")