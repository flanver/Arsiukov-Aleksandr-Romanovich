n = int(input())
a = list(map(int, input().split()))
m = 0
for i in range(n):
    if a[i] > m:
        m = a[i]
        print(m)
for i in range(n-1, -1, -1):
    print(a[i], end=" ")