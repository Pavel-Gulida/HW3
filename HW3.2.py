
l1 = [12, 3, 4, 10]
l2 = [1]
l3 = []
l4 = [12, 3, 4, 10, 8]
mass = l1

if len(mass) > 1:
    mass.insert(0, mass.pop())
print(mass)


