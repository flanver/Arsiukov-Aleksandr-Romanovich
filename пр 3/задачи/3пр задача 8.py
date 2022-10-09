def F(a, b, c):
    if a == b == c:
        return 3
    elif a != b != c != a:
        return 0
    else:
        return 2
a = int(input())
b = int(input())
c = int(input())
print(F(a, b, c))