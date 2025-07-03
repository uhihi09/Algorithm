a = float(input())
b = float(input())
cnt = a/(b*b)
if cnt > 25:
    print("Overweight")
elif 18.5 <= cnt <= 25:
    print('Normal weight')
else:
    print("Underweight")