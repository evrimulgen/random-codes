import math
def funct(n1, n2):
	count = 0
	sec_digit = 0
	third_digit = 0
	for i in n1:
		sec_digit = 0
		#for j in range(n2):
		for x in range(int(math.pow(n2, n2) * math.pow(n2, n2))):
			try:
				print(str(i) + str(n1[sec_digit]) + str(n1[third_digit]))
				third_digit += 1
				if third_digit >= len(n1):
					third_digit = 0
					sec_digit += 1
				count += 1
			except:
				continue
	print(count)

funct([1,2,3,4,5,6], 3)
