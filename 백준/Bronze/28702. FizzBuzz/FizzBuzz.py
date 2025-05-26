a = input()
b = input()
c = input()
ans = 0
if str.isdigit(a) == True:
    ans = int(a)+3
elif str.isdigit(b) == True:
    ans = int(b)+2
elif str.isdigit(c) == True:
    ans = int(c)+1
if ans%3 == 0 and ans%5==0:
    print("FizzBuzz")
elif ans%3 == 0 and ans%5!=0:
    print("Fizz")
elif ans%3 != 0 and ans%5 == 0:
    print("Buzz")
elif ans%3 != 0 and ans%5 != 0:
    print(ans)