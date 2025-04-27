a = int(input())
cnt = 0
b = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you","Never gonna stop"]
for i in range(a):
    c = input()
    if c not in b:
        cnt = 1
if cnt == 1:
    print("Yes")
else:
    print("No")