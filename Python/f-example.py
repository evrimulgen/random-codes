import math
r = 10

f'Area of a circle with radius {r}: {math.pi*r**2}'

for i in range(20):
	f'{i} box{"es"if i!=1 else ""}'


for i in range(20):
	f'{i} is {"even" if i % 2 == 0 else "odd"}'

for i in range(10):
	f'{i * "sa"}'
