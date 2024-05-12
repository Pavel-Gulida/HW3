
l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3]
l3 = [1, 2, 3, 4, 5]
l4 = [1]
l5 = []
mass = l5

middle = len(mass) // 2 + len(mass) % 2
mass1 = [mass[0:middle], mass[middle:len(mass)]]
print(mass1)
