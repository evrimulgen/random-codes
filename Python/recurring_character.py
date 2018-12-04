"""Give a word, if it has a recurring character it will print out the first one"""

inp = str(input())

def func(inp):
	out = None
	for i in inp:
		finder = inp.find(i)
		full = inp[:finder] + inp[finder+1:]
		for j in range(len(full)):
			if i == full[j]:
				out = i
				return print(out)
	return print(out)

func(inp)

