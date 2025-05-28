n,a,b = map(int,input().split())
binan = 0
chingchan = 0
for i in range(n):
    chingchan += a
    binan += b
    if chingchan < binan:
        chingchan,binan = binan,chingchan
    elif binan == chingchan:
        binan -= 1
print(chingchan+1,binan+1)