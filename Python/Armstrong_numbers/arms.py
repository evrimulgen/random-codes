def calcu():
	num = int(input("number: "))
	if num > 100 and num <1000:
		first_num = int(list(str(num))[0])
		second_num = int(list(str(num))[1])
		third_num = int(list(str(num))[2])
		output = first_num**3 + second_num**3 + third_num**3
		print(output, output == num)
		return calcu()
		# print(output == num)
	else:
		print("The number cannot be lower than 100 and higher than 999")
		return calcu()

# calcu()

for i in range(100, 1000):
	first_num = int(list(str(i))[0])
	second_num = int(list(str(i))[1])
	third_num = int(list(str(i))[2])
	if first_num**3 + second_num**3 + third_num**3 == i:
		print(i, True)
	else:
		pass