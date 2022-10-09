def F(a, b, l, N):
    return (a*2+b*2)*(N-1)+l*2+a
a=int(input()) #  a расстояние между рядами
b=int(input()) #  b расстояние между отверстиями
l=int(input()) #  l длина ост 2 шнурков
N=int(input()) #  N кол-во отверстий
print(F(a, b, l, N))