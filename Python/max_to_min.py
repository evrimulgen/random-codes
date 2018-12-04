def c(x):
	for i in range(len(x)):
		if x[i] == max(x):
			x[i] = min(x)
			print(x)

b = [1, 22, 4, 55, 7, 99, 0, 88, 6, 3, 1, 34, 5, 6, 7, 324, 25]
c(b)