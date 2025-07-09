cnt = []
for i in range(9):
    cnt.append(input())
if cnt.count("Lion") >= cnt.count("Tiger"):
    print("Lion")
else:
    print("Tiger")