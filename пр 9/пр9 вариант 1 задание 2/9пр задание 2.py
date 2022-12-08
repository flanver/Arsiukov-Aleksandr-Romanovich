import random
from pprint import pprint
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(N)] for j in range(N)]
pprint(B)
for x in range(len(B)) :
    idx = B[x].index(min(B[x]))
    B[x][idx], B[x][0] = B[x][0], B[x][idx]
    idx = B[x].index(max(B[x]))
    B[x][idx], B[x][-1] = B[x][-1], B[x][idx]
pprint(B)