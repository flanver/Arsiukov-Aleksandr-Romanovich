print('введите количество секунд')
seconds = int(input())
minutes = 0
hours = 0
days = 0
if seconds >=60:
    minutes = seconds // 60
    seconds = seconds % 60
if minutes >=60:
    hours = minutes // 60
    minutes = minutes % 60
if hours >=24:
    days = hours // 24
    hours = hours % 24
print(days,':',hours,':',minutes,':',seconds)
