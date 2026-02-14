a,b = map(int,input().split())

matrix = []

black = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB',
         'BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']

white = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW',
         'WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']

ans = 1000000000

for i in range(a):
    matrix.append(input())

for i in range(len(matrix)-7):
    for j in range(len(matrix[i])-7):
        black_cnt = 0
        white_cnt = 0
        for k in range(8):
            for l in range(8):
                if matrix[i+k][j+l] != black[k][l]:
                    black_cnt += 1
                if matrix[i+k][j+l] != white[k][l]:
                    white_cnt += 1
        ans = min(ans,black_cnt,white_cnt)
print(ans)