# convert binary number to decimal
import math
T = int(input())
res = []
for i in range(T):
    n = int(input())
    b=1
    val=0
    while n>0:
        r = n % 10
        val = val + (r * b)
        n = math.floor(n / 10)
        b*=2
    res.append(val)
[print(i,sep='\n') for i in res]
# print(n)