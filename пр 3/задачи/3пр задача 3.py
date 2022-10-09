n=int(input())
m=0
d=0
h=0
m=n%60
h=n//60
if h > 23:
    h=h%24
print(h,':',m)