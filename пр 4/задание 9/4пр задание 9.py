n=int(input())
l=0
f2=1
s=0
h=0
for i in range(0,n):
    h=h+l
    s=l+f2
    l=f2
    f2=s
print(h)