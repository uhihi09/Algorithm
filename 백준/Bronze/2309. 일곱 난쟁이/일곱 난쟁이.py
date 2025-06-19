cnt = []
def love():
    for i in range(9):
        cnt.append(int(input()))
    for ii in range(9):
        for iii in range(ii+1,9):
            if sum(cnt) - cnt[ii] - cnt[iii] == 100:
                ans = [cnt[iv] for iv in range(9) if iv != ii and iii != iv]
                ans.sort()
                for v in ans:
                    print(v)
                return
love()