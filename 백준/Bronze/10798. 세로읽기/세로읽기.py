love = []
ans = ''
cnt = -1
for i in range(5):
    love.append(list(input()))
for i in range(max(map(len,love))):
    cnt += 1
    for ii in range(len(love)):
            try:
                ans += love[ii][i]
            except:
                pass
print(ans)