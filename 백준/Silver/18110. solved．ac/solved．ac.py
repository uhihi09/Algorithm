import sys
input = sys.stdin.readline
def answer(nu,array):
    if nu == 0:
        return 0
    else:
        maxin = max(array)
        minin = min(array)
        if maxin == minin:
            return array[0]
        else:
            array.remove(maxin)
            array.remove(minin)
        avg = round(nu * (15/100)+0.000001)
        array.sort()
        ans = []
        for idx in range(avg-1,len(array)-avg+1):
            ans.append(array[idx])
        return round(sum(ans) / len(ans) + 0.000001)

a = int(input())
cnt = []
for i in range(a):
    cnt.append(int(input()))
print(answer(a,cnt))