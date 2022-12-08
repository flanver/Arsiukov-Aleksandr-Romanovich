import math
def F(fig):
    if fig == 'круг':
        d=int(input('введите диаметр:'))
        n=math.pi*d
    elif fig == 'треугольник':
        a=int(input('введите основание:'))
        b=int(input('введите высоту:'))
        n=(a*b)/2
    elif fig == 'квадрат' or fig =='прямоугольник':
        a=int(input('введите основание:'))
        b=int(input('введите высоту:'))
        n=a*b
    else: 
        return 'не понимаю что за фигура, попробуйте сново'
    return n
fig=str(input('введите название фигуры:'))
print('площадь фигуры',fig,'=',F(fig),)