from pprint import pprint
f = open ("C:\\Users\\fotog\\Desktop\\работы инфа\\Arsiukov-Aleksandr-Romanovich\\пр 10\\10пр задание 1\\АрсюковА.Р._У-224_vvod.txt", 'r')
l = []
l = [ line.split() for line in f]
with open ("C:\\Users\\fotog\\Desktop\\работы инфа\\Arsiukov-Aleksandr-Romanovich\\пр 10\\10пр задание 1\\АрсюковА.Р._У-224_vivod.txt", 'w') as file:
    file.write(str(l))