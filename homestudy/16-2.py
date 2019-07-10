h, y = input().split(',')

h = int(h)
y = int(y)

pyo = []

for i in range(h):
    pyo.append([])
    for l in range(y):

        pyo[i].append((i)*(l))

print(pyo)
