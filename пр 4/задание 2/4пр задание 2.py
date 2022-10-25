n=int(input())
h=int(input())
if n<h:
    while h>n:
        print(n)
        n+=1
    print(h)
else:
    while h<n:
        print(n)
        n -=1
    print(n)