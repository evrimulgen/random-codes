import json
import urllib2
import time

def get_coins(coin_file):
	num_coins = len(open(coin_file).readlines())
	with open(coin_file) as f:
	    coins = f.read().splitlines()
	f.close()
	return num_coins, coins

def get_sell_data(coin):
	url = "https://www.cryptopia.co.nz/api/GetMarketOrders/" + coin + "_BTC"
	data = json.load(urllib2.urlopen(url))
	data = data["Data"]
	if data is None:		#needs work 
		return -1
	data = data["Sell"]
	if len(data) == 0:
		return -1			#needs work	
	return data

def get_pump_indicator(data, limit):
	sum = 0
	result = 0
	for x in range(0,100):
		sum += float(data[x]["Total"])
		if sum >= limit:
			break
		result = (float(data[x]["Price"])/float(data[0]["Price"]))
	return result

def myformat(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')


coin_file = 'all_coins.txt'
output_file = 'all_prospective_coins'
limit1 = 0.5
limit2 = 1.5
limit3 = 2.0
limit4 = 2.5


if __name__ == "__main__":

	num_coins, coins = get_coins(coin_file)
	
	result = []
	for x in range(0,num_coins):
		coin = coins[x]

		data = get_sell_data(coin)


		if data == -1:
			indicator1 = -1
			indicator2 = -1
			indicator3 = -1
			indicator4 = -1
		else:
			indicator1 = get_pump_indicator(data, limit1)
			indicator2 = get_pump_indicator(data, limit2)
			indicator3 = get_pump_indicator(data, limit3)
			indicator4 = get_pump_indicator(data, limit4)

		toprint= coin + ", " + myformat(indicator1) + "  " + myformat(indicator2) + "  " + myformat(indicator3)  + "  " + myformat(indicator4) 
		print toprint
		result.append(toprint)

	with open(output_file+".txt", 'w+') as f:
		for x in range(0,num_coins):
			f.write(result[x] + '\n')
		f.close()
	
	#print indicator

