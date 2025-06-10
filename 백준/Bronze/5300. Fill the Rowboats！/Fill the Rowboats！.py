a = int(input())
ans = []
for i in range(1,a+1):
    if i % 6 == 0:
        ans.append(i)
        ans.append("Go!")
    else:
        ans.append(i)
if ans[-1] != 'Go!':
    ans.append('Go!')
for i in ans:
    print(i,end=" ")