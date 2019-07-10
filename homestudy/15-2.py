import math

radius = input().split(',')

l = len(radius)

r = list(map(lambda x: str(round(int(x)**2*math.pi,2)), radius))


for i in range(l-1):
    print(r[i]+', ' ,end='')

print(r[l-1])
