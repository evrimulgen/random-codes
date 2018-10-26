# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# letters2 = ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "d", "c", "e", "f", "g" , "h"]

# def code(sentence, order):
# 	if order == "encrypt":
# 		for x in range(0, sentence.__len__()):
# 			for i in range(0, 26):
# 				try:
# 					if letters[i].lower() == list("".join(sentence.split(" ")))[x].lower():
# 						print(letters2[i], end=" ", flush=True)
# 				except:
# 					pass
# 	elif order == "decrypt":
# 		for x in range(0, sentence.__len__()):
# 			for i in range(0, 26):
# 				try:
# 					if letters2[i].lower() == list("".join(sentence.split(" ")))[x].lower():
# 						print(letters[i], end=" ", flush=True)
# 				except:
# 					pass
# 	else:
# 		print("order didnt recieved correctly. Try again...")
# 		return code(input("What is your sentence? "), input("if want to Decrypt type 'decrypt' or else type 'encrypt': "))
# 	print("\r")


# code(input("What is your sentence? "), input("if want to Decrypt type 'decrypt' or else type 'encrypt': "))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letters2 = ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "d", "c", "e", "f", "g", "h"]
line = []
line2 = []

def code(sentence, order):
	if order == "encrypt":
		for x in range(0, sentence.__len__()):
			if sentence[x] == " ":
				line.append(" ")
			for i in range(0, 25):
				try:
					if letters[i].lower() == sentence[x].lower():
					    line.append(letters2[i])
				except:
					pass

		newline = "".join(line)

		for x in range(0, newline.__len__()):
			if newline[x] == " ":
				line2.append(" ")
			for i in range(0, 25):
				try:
					if letters2[i].lower() == newline[x].lower():
						line2.append(letters[i])
				except:
					pass

		newline2 = "".join(line2)
		print("'{}' encrypted as '{}'".format("".join(line2), newline))

    elif order == "decrypt":
        for x in range(0, sentence.__len__()):
			if sentence[x] == " ":
				line.append(" ")
			for i in range(0, 26):
				try:
					if letters2[i].lower() == sentence[x].lower():
					    line.append(letters[i])
				except:
					pass
		print("'{}' decrypted as '{}'".format(sentence, "".join(line)))
	else:
		print("The order didnt recieved correctly. Try again...")


code(input("What is your sentence to encrypt"), "decrypt")