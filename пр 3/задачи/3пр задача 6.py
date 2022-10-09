def F(a, b, c, d):
    if (a%2 == b%2) == (c%2 == d%2):
        return 'да'
    else:
        return 'нет'
a=int(input()) #  a 1
b=int(input()) #  b 2
c=int(input()) #  c 1
d=int(input()) #  d 2
print(F(a, b, c, d))