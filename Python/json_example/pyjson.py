import json

merve = {
	"name":"Merve",
	"surname":"yonyul",
	"age": 18,
	"beautiful" : False
}
mirkan = {
	"name" : "Mirkan",
	"surname": "Kılıç",
	"age": 24,
	"beautiful" : True
}

jfile = open('/home/mirkan/Desktop/json_example/pyjson.txt', 'a')
json.dump(merve, jfile)
jfile.close()

jfile = open('/home/mirkan/Desktop/json_example/pyjson.txt', 'a')
json.dump(mirkan, jfile, ensure_ascii=False) # if False KILIC wont be printed normally xd
jfile.close()

jfile = open('/home/mirkan/Desktop/json_example/pyjson.txt', 'a')
json.dump(merve, jfile)
jfile.close()

