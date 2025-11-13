n, a, b = map(int, input().split())
s, t = map(int, input().split())
def location(x):
    if 1 <= x <= a:
        return "outside1"
    elif b <= x <= n:
        return "outside2"
    else:
        return "city"
s_loc = location(s)
t_loc = location(t)
if s_loc == "city" and t_loc == "city":
    print("City")
elif "outside" in s_loc and "outside" in t_loc:
    if s_loc == t_loc:
        print("Outside")
    else:
        print("Full")
else:
    print("Full")