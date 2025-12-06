import sys
input = sys.stdin.readline
a, b = map(int, input().split())
result = [str(a // b)]
a %= b
if a:
    result.append(".")
    for _ in range(1000):
        a *= 10
        result.append(str(a // b))
        a %= b
        if a == 0:
            break

print("".join(result))