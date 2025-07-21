a,b,c = map(int,input().split())
fizz = 0
buzz = 0
fizzbuzz = 0
for i in range(1,a+1):
    if i%b ==0 and i%c == 0:
        fizzbuzz += 1
    elif i%b == 0:
        fizz += 1
    elif i%c == 0:
        buzz += 1
print(fizz,buzz,fizzbuzz)