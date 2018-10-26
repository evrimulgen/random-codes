I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

full_number = str(input("What is the number that you want to be converted\n"))
forth_digit = list(full_number)[-4]
third_digit = list(full_number)[-3]
second_digit = list(full_number)[-2]
last_digit = list(full_number)[-1]






if int(third_digit) >= 5:
	if int(third_digit) == 5:
		third_digit = "D"
	if int(third_digit) == 6:
		third_digit = "DC"
	if int(third_digit) == 7:
		third_digit = "DCC"
	if int(third_digit) == 8:
		third_digit = "DCCC"
	if int(third_digit) == 9:
		third_digit = "CM"

if int(second_digit) >= 5:
	if int(second_digit) == 5:
		second_digit = "L"
	elif int(second_digit) == 6:
		second_digit = "LX"
	elif int(second_digit) == 7:
		second_digit = "LXX"
	elif int(second_digit) == 8:
		second_digit = "LXXX"
	elif int(second_digit) == 9:
		second_digit = "XC"

if last_digit == "1":
	last_digit = "I"
elif last_digit == "2":
	last_digit = "II"
elif last_digit == "3":
	last_digit = "III"
elif last_digit == "4":
	last_digit = "IV"
elif last_digit == "5":
	last_digit = "V"
elif last_digit == "6":
	last_digit = "VI"
elif last_digit == "7":
	last_digit = "VII"
elif last_digit == "8":
	last_digit = "VIII"
elif last_digit == "9":
	last_digit = "IX"

if second_digit == "1":
	second_digit = "X"
elif second_digit == "2":
	second_digit = "XX"
elif second_digit == "3":
	second_digit = "XXX"
elif second_digit == "4":
	second_digit = "XL"

if third_digit == "4":
	third_digit = "CD"
elif third_digit == "3":
	third_digit = "CCC"
elif third_digit == "2":
	third_digit = "CC"
elif third_digit == "1":
	third_digit = "C"



print(third_digit+second_digit+last_digit)
