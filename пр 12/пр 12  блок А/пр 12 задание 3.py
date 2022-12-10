n = int(input())
a = 0
while n > 0:
    d = n % 10
    n = n // 10
    a = a * 10
    a = a + d  
print(a)