"""	
To calculate what is digit value of an exponential number top of two or three.
One can multiply the numbers or,
One has to take the exponential number's logarithm on 10 base then add 1 to outcome.
The formula: 	log(2) === 0,301
				log(3) === 0.477
"""
import math

def exponential(num, exponential_num):
	two = num
	for i in range(exponential_num-1):
		num *= two

	digit_value = len(str(num))
	try:
		return print(num, "\n", math.pow(two, exponential_num), sep="")
	except:
		return print(num, "\n", digit_value, sep="")

num, exponential_num = int(input()), int(input())
exponential(num, exponential_num)
