import sys

def fabo(number):
	n = number
	prevnum = 1
	num = 1
	while n:
		num = num + prevnum
		prevnum = num - prevnum
		n -= 1 
	return num

print(fabo(int(sys.argv[1])))

# function fab(n) {let number = n; let prevnum = 1; let num = 1; while(number) {num = num + prevnum; prevnum = num - prevnum; number -= 1} return num}