import random

line = [["Hello all{}".format("." * random.randint(0,4)), 
		"Do you know Supreme.Investements?",  
		"They make awesome Pump and Dump again{}".format("." * random.randint(0,4))
		],[
		"Do you guys remember Supreme Investments{}".format("?" * random.randint(0,3)),
		"Supreme Pumps makes awesome pumps",
		"Supreme pumps owners are awesome and friendly",
		"I suggest you guys to join them {}".format(":)" * random.randint(0,2))
		],[
		"I heard about Supreme_Investments {}".format("xD " * random.randint(0,2)),
		"Supreme Pumps makes Pumps to Mars",
		"LOL",
		"I suggest you guys to join them {}".format(":)" * random.randint(0,2))
		],[
		"Hey people{}".format("!" * random.randint(0,2)),
		"I love upreme-investments they made me rich from last pump",
		"",
		"i want you to be rich as well {}".format(":)" * random.randint(0,2))
		],[
		"sup",
		"if anybody looking for a good pump and dump group{}".format("?" * random.randint(0,3)),
		"if yes I know a group named Sup.reme pumps"
		]]

def pr():
	rd = random.randint(0, len(line) -1)
	for i in range(len(line[rd])):
		print(line[rd][i])

pr()