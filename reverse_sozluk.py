sozluk = {'elma': 'apple', 'muz': 'banana', 'uzum': 'grapes', 'havuc': 'carrot'}

reversed_one = {i:j for j,i in sozluk.items()}

reversed_two = tuple(map(lambda x,y: x+y, (i for i in sozluk.values()), (i for i in sozluk.keys())))
reversed_three =  list(map(lambda x,y: dict({y:x}), (i for i in sozluk.keys()), (i for i in sozluk.values())))

with_map_final =  dict(tuple(map(lambda x,y: (y,x), (i for i in sozluk.keys()), (i for i in sozluk.values()))))

python_way = dict([(value, key) for key, value in sozluk.items()])

def getit(value):
	import pdb
	pdb.set_trace()
	splitted = str(sozluk).split("'")

	for i in range(len(splitted)):
		if splitted[i] == value:
			print(splitted[i - 2])

def reverse_one(value):
	for i, j in sozluk.items():
		if str(i) == value:
			reversed_sozluk = dict(tuple(map(lambda x,y: (y,x) if str(value) == str(i) else (x,y), (i for i in sozluk.keys()), (i for i in sozluk.values()))))
			return print(reversed_sozluk)
		elif str(j) == value:
			reversed_sozluk = dict(tuple(map(lambda x,y: (y,x) if str(value) == str(j) else (x,y), (i for i in sozluk.keys()), (i for i in sozluk.values()))))
			return print(reversed_sozluk)
	return print(sozluk)

def easy_one():
	b = {}
	for i,j in sozluk.items():
		b[j] = i

reverse_one(getit(12))