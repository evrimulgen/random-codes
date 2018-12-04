import sys

def factorialRecursive(number):
	if number < 1:
		return 1
	else:
		return number * factorialRecursive(number -1)

print(factorialRecursive(int(sys.argv[1])))