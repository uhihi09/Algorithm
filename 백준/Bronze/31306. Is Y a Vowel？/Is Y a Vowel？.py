a = list(input())
mo = ['a','e','i','o','u']
ans1 = 0
ans2 = 0
for i in a:
    if i in mo:
        ans1 += 1
ans2 = ans1+a.count("y")
print(ans1,ans2)