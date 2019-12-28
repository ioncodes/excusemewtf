import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os


alphabet = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
alphabet_length=len(alphabet)
iv = hashlib.md5(b"infernoCTF").digest()


data = b"Double AES encryption for twice the strength.Win"
flag = "lIZMVkA+pbiOxh3nNdV2bWz3gXovIy4fG7yCHa5FT44="

#keys found from middleman.py
key1 = "0000000000000000000000000000021Q"
key2 = "00000000000000000000000000000(iA"

#Double encrypt the plaintext with keys to verify its correct
##########encrypt mode
cipher_encrypt = AES.new(key1.encode(), AES.MODE_CBC, iv=iv)
ciphertext = cipher_encrypt.encrypt(data)
print(base64.b64encode(ciphertext))

cipher_encrypt = AES.new(key2.encode(), AES.MODE_CBC, iv=iv)
ciphertext = cipher_encrypt.encrypt(ciphertext)
print(base64.b64encode(ciphertext)) #should be sample in the challenge

#Double decrypt the flag with the keys
aes = AES.new(key2.encode(), AES.MODE_CBC, iv=iv)
decd = aes.decrypt(base64.b64decode(flag))
aes = AES.new(key1.encode(), AES.MODE_CBC, iv=iv)
decd = aes.decrypt(decd)
print(decd.decode())

