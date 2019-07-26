import requests

parameters = {"username": "mirkanbaba1@gmail.com", 
			"token": "f8c8988e6b3b8aaa9a91587e72ff4626"}
response = requests.get("http://www.getsmscode.com/do.php?action=login&username=[{}]&token=[{}]".format(parameters["username"], parameters["token"]))

print(response.content)