p=0
t=1
max=1
while True:
    n=int(input())
    if n==0:
        break
    elif n==p:
        t+=1
    elif n!=p:
        t = 1
    if max<t:
        max=t
    p=n
print(max)