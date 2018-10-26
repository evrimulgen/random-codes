accomplished_invites = int(input())

noob        = 0
affiliate   = 1
conselor    = 10
minister    = 20
senator     = 50
ambassador  = 150
chairman    = 500

if accomplished_invites > 0 and accomplished_invites < 1:
    current_rank = noob
    next_rank = affiliate
    new_rank = 'affiliate'
elif accomplished_invites > 1 and accomplished_invites < 9:
    current_rank = affiliate
    next_rank = conselor
    new_rank = 'conselor'
elif accomplished_invites > 10 and accomplished_invites < 20:
    current_rank = conselor
    next_rank = minister
    new_rank = 'minister'
elif accomplished_invites > 20 and accomplished_invites < 50:
    current_rank = minister
    next_rank = senator
    new_rank = 'senator'
elif accomplished_invites > 50 and accomplished_invites < 150:
    current_rank = senator
    next_rank = ambassador
    new_rank = 'ambassador'
elif accomplished_invites > 150 and accomplished_invites < 500:
    current_rank = ambassador
    next_rank = chairman
    new_rank = "chairman"
elif accomplished_invites > 500:
    current_rank = chairman
    next_rank = accomplished_invites
    new_rank = None

invites_to_rank_up = next_rank - accomplished_invites
print("You currently have {} invites. Need {} more invites become {}".format(accomplished_invites, invites_to_rank_up, new_rank))


























































# import asyncio

# async def hey():
# 	print('hello world')

# loop = asyncio.get_event_loop()
# # Blocking call which returns when the hello_world() coroutine is done
# loop.run_until_complete(hey())
# # loop.close()












































# class Sinif():
# 	__s = 's'				#gizli cagirilamaz
# 	s = 's'
# 	def __init__(self):
# 		self.a = '123'

# 	def __baba(self):		#gizli cagirilamaz
# 		print('sa')

# 	def __baba__(self):
# 		print('sa')




















































# class Mat():
# 	# def __init__(self, sayi):
# 		# self.sayi = int(sayi)

# 	@staticmethod
# 	def pi():
# 		return 22/7

# 	@staticmethod
# 	def karekok(sayi): 			# Hem ornek hem de sinif metoduyla erisilebiliyorlar
# 		return sayi ** 0.5		# Mat.pi() /// Mat().pi()

# 	def kk(self, sayi):
# 		print(sayi ** 0.5)

# 	def pi_ornek(self):			# Mat().pi() /// Sadece ornek metoduyla
# 		return 22/7

# 	@classmethod
# 	def pi_ornek(cls):			# Mat.pi()   /// Sadece sinif metoduyla
# 		return 22/7




















































# class Sinif():
# 	veri = '123'
# 	def __init__(self):
# 		self.veri = 'veri'
# 		print('1234')

# 	def orn(self):
# 		return self.veri

# 	@classmethod
# 	def siniff(cls):
# 		return cls.__init__()

# 	@staticmethod
# 	def statik_metot():
# 		print('merhaba statik metot!')

# 	def a(self):
# 		print('s')























































# class Gir():
# 	def __init__(self, msj='Whats your name?'):
# 		answer = input(msj)
# 		print('sa {}'.format(answer))

# 	@classmethod
# 	def surname(cls):
# 		msj = 'Whats your surname?'
# 		return cls(msj)

# 	@classmethod
# 	def lakab(self):
# 		lak = 'Whats your lakab?'
# 		return self(lak)



















































# class Sorgu():
# 	def __init__(self, deger=None, sira=None):
# 		self.liste = 	[('b1','2','3'),
# 		 				('4','5','6'),
# 		 				('7','8','9')]

# 		if not deger and not sira:
# 			l = self.liste
# 		else:
# 			l = [li for li in self.liste if deger == li[sira]]

# 		for i in l:
# 			print(*i, sep=', ')

# 	@classmethod
# 	def ilk(cls, ilki):
# 		cls(ilki, 0)

	# def bul(self, sayi=None):
	# 	if sayi == '1':
	# 		return self.liste[0]
	# 	if sayi == '2':
	# 		return self.liste[1]
	# 	if sayi == '3':
	# 		return self.liste[2]

	# def yine_bul(self, sayi):
	# 	d = { 	'1'	: self.bul('1'),
	# 			'2'	: self.bul('2'),
	# 			'3'	: self.bul('3'),
	# 		}

	# 	cumle = []
	# 	#k = cumle.append(d)
	# 	for oge in d.get(sayi, self.liste):
	# 		cumle.append(oge)
	# 		print(cumle)

	# # 	#print(cumle, sep='-')
	# def kaka(self):
	# 	print([li for li in self.liste])























# class Sinif():
# 	benim_sinif = 0

# 	def __init__(self, param1, param2):
# 		self.param1 = param1
# 		self.param2 = param2
# 		self.onun_sinif = 0

# 	#@classmethod
# 	def onunn_sinif(self):
# 		self.onun_sinif += 1
# 		return self.onun_sinif

# 	@classmethod
# 	def benim_siniff(cls):
# 		cls.benim_sinif +=1
# 		return cls.benim_sinif















































# import random

# class Pokemon():
# 	pokemon_name = [] #ornek.Pokemon.pokemon_name


# 	def __init__(self, name): # balba = ornek.Pokemon('balbazar')
# 		self.name = name
# 		self.element = []
# 		self.add_pokemon()

# 	def add_pokemon(self):
# 		self.pokemon_name.append(self.name)
# 		print('{} named pokemon has been added to the list'.format(self.name))

# 	@classmethod
# 	def pokemon_list(cls):
# 		print('Pokemon list...')
# 		for pokemon in cls.pokemon_name:
# 			print(pokemon)

# 	def pokemon_element(self):
# 		if self.element == []:
# 				print('no element for current Pokemon')
# 		else:
# 			print('{}"s pokemon element is'.format(self.name))
# 			for elementi in self.element:
# 				print(elementi)

# 	def add_element(self, element): # ornke.Pokemon('balbazar').add_element('leaf')
# 		self.element.append(element)

# 	def remove_element(self, element):
# 		self.element.remove(element)

# 	@classmethod
# 	def random_pokemon(cls):
# 		print('Random Pokemon is getting choosed...')
# 		print(random.choice(cls.pokemon_name))






































# class Adam():
# 	def __init__(self):
# 		self.kabiliyetler = []
# 		self.adi = ''
# 		self.soyadi = ''

# 	def all():
# 		print(Adam.adi)
# 		print(Adam.soyadi)













































# class Calisan:
# 	def __init__(self):
# 		self.kabiliyet = []
# 		self.yas = []

# 	def sor(self):
# 		self.kabiliyet = input("kabiliyetin ne?")
# 		return self.yazdir()

# 	def ali(self):
# 		self.yas = input("yasin kac?")
# 		return self.sor()

# 	def yazdir(self):
# 		print('{} isen ise alindin, yasin da {} cok iyi'.format(self.kabiliyet, self.yas))

# 	def calistir(self):
# 		#self.sor = self.sor()
# 		self.ali = self.ali()
# 		#self.yazdir = self.yazdir()


# Calisan().calistir()







































# class HarfSayacı:
#     def __init__(self):
#         self.sesli_harfler = 'aeıioöuü'
#         self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
#         self.sayaç_sesli = 0
#         self.sayaç_sessiz = 0

#     def kelime_sor(self):
#         return input('Bir kelime girin: ')

#     def seslidir(self, harf):
#         return harf in self.sesli_harfler

#     def sessizdir(self, harf):
#         return harf in self.sessiz_harfler

#     def artır(self):
#         for harf in self.kelime:
#             if self.seslidir(harf):
#                 self.sayaç_sesli += 1
#             if self.sessizdir(harf):
#                 self.sayaç_sessiz += 1
#         return (self.sayaç_sesli, self.sayaç_sessiz)

#     def ekrana_bas(self):
#         sesli, sessiz = self.artır()
#         mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
#         print(mesaj.format(self.kelime, sesli, sessiz))

#     def çalıştır(self):
#         self.kelime = self.kelime_sor()
#         self.ekrana_bas()

# if __name__ == '__main__':
#     sayaç = HarfSayacı()
#     sayaç.çalıştır()

