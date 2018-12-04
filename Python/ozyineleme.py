class Pokemon():
	pokemon_name = []


	def __init__(self, name, element):
		self.name = name
		self.element = element
		self.add_pokemon()

	def add_pokemon(self, name):
		self.pokemon_name.append(self.name)
		print('{} named pokemon has been added to the list'.format(self.name))
















































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

