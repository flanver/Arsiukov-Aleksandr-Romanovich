print('Введите свой возраст')
age = int(input())
print('Введите своё имя')
name = str(input())
if name != 'иван' :
    if age > 0 and age < 75:
      if age >=16:
           print('Поздравляем вы поступили в ВГУИТ')
      else:
           print('Сначала нужно окончить школу! И вам осталось учиться',16-age,'лет')
else:
    print('увы но вы иван')
