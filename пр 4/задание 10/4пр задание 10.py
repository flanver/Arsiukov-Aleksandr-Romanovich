n=int(input())
k=int(input())
f=0
v=1
s=0
m=0
for i in range(0,n+k-1):
    if i>=n-1:
        m=m+f   
    s=f+v
    f=v
    v=s    
print(m)
