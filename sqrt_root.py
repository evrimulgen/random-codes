import math, time

def sqrt_root(num):
	while True:
		num = num + 1
		if str(math.sqrt(num)).split(".")[1] == "0":
			print("{}'s square root is {}".format(num, math.sqrt(num)))
			time.sleep(0.5)

sqrt_root(1)