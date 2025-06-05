a = int(input())
b = int(input())
if 1 <= b-a <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= b-a <= 30:
    print("You are speeding and your fine is $270.")
elif b-a >= 31:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")