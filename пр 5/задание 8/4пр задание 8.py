b=0
t=1
m=1
while True:
    n=int(input())
    if n==0:
        break
    elif n==b:
        t+=1
    elif n!=b:
        t = 1
    if m<t:
        m=t
    a=n
print(m)