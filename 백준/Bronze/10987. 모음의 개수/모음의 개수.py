a = list(input())
word = ["a","e","i","o","u"]
cnt = 0
for i in a:
    if i in word:
        cnt +=1
print(cnt)