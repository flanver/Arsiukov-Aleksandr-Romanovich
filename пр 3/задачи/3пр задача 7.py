def F(a):
    if (a % 4 == 0 and a%100 != 0) or (a%400 == 0):
        return 'да'
    else:
        return 'нет'
a=int(input())
print(F(a))