def F(n, m, k):
    if k <= n * m and ((k % n == 0) or (k % m == 0)):
        return 'да'
    else:
        return 'нет'
n = int(input())
m = int(input())
k = int(input())
print(F(n, m, k))