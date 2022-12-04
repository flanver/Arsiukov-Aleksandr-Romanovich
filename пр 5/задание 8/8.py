c=0
n=int(input())
ch=n
max=0
while n!=0:
    if ch==n:
        c+=1
        if max < c:
            max=c
    else:
        ch=n
        c=1
    n=int(input())
print(max)