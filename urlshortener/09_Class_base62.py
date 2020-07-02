import hashlib

class Base62():

	_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def decode(self,url):
		md5 = hashlib.md5()
		md5.update(url.encode('utf-8'))
		hexa = md5.hexdigest()
		decimal = int(hexa,16)

		array_base62 = []
		base62 = ''
		while decimal > 0:
			array_base62.append(int(decimal%62))
			decimal = decimal//62 

		for posicion in reversed(array_base62):
			base62 += self._alphabet[posicion]

		return base62 

instancia = Base62()

print(instancia.decode("https://github.com/delight-im/ShortURL/blob/master/Python/shorturl.py"))