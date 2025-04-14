a = int(input())
b = list(map(int, input().split()))
odd = 0
even = 0
for i in range(a):
    if b[i]%2 == 0:
        even += 1
    else:
        odd += 1
if odd >= even:
    print("Sad")
else:
    print("Happy")