from itertools import product

a = []
b = []
for _ in range(1):
    a.append(input().split())
    if len(a) == 1:
        b.append(input().split())
new_a = []
new_b = []

for i in a:
    for j in i:
        new_a.append(int(j))


for i in b:
    for j in i:
        new_b.append(int(j))

z = []
for i in list(product(new_a, new_b)):
    z.append(str(i))

print('')

