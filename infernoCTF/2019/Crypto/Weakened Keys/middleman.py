import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

alphabet = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
alphabet_length=len(alphabet)
iv = hashlib.md5(b"infernoCTF").digest()
data = b"Double AES encryption for twice the strength.Win"
enc = base64.b64decode('0mu0T97looX5/Oorw8ASGxfqMqrNoFajZupXrjtIAj7ECJdQXZzEmbEwdRV2J2MI')

f1 = open("enc.txt", "w")
f2 = open("dec.txt", "w")
total=alphabet_length**3
for i in range(0,total):
	### generate key
	keynum = i
	key=[]
	for  j in range(32):
		rem = keynum % alphabet_length
		div = keynum // alphabet_length
		keynum = div
		key.append(alphabet[rem])
		if (div == 0):
			break
	key = ''.join(key).rjust(32, '0')
	#print(key)
	##########encrypt mode
	cipher_encrypt = AES.new(key.encode(), AES.MODE_CBC, iv=iv)
	ciphertext = cipher_encrypt.encrypt(data)
	f1.write(base64.b64encode(ciphertext).decode() + "\n")

	##########decrypt mode
	aes = AES.new(key.encode(), AES.MODE_CBC, iv=iv)
	decd = aes.decrypt(enc)
	f2.write(base64.b64encode(decd).decode() + "\n")
	#print(str(i) + "/" +  str(total), end='\r')

print("Finished generating. Now checking common")
os.system("awk 'NR==FNR{arr[$0];next} $0 in arr' enc.txt dec.txt")