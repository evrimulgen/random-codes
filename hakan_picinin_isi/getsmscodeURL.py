import requests
class SMS:

	login = requests.get('http://www.getsmscode.com/do.php?action=login&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626').text

	getmobile = requests.get('http://www.getsmscode.com/do.php?action=getmobile&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10').text

	getsms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(SMS.getmobile)).text

	addblack = requests.get('http://www.getsmscode.com/do.php?action=addblack&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}'.format(SMS.getmobile)).text

	mobilelist = requests.get('http://www.getsmscode.com/do.php?action=mobilelist&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626').text

	def getsms_():
		for i in range(15):
			sms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile={}&author=mirkanbaba1@gmail.com'.format(SMS.getmobile)).text
			if SMS.getsms != 'Message|not receive':
				code = sms.split(">")[1]

				pass
			else:
				pass


# getsms = requests.get('http://www.getsmscode.com/do.php?action=getsms&username=mirkanbaba1@gmail.com&token=f8c8988e6b3b8aaa9a91587e72ff4626&pid=10&mobile=8617049806616&author=mirkanbaba1@gmail.com').text
