import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# set the flag value to some secret message
flag = 'Double AES encryption for twice the strength.Win'

data = flag.encode('utf-8')

# Local political concerns about strong encryption,
# means first 224 bits of all keys have been set to 0.

# temp keys for testing
key1 = get_random_bytes(32) 
key2 = get_random_bytes(32)
key1=b"infernoCTF123412"
key2=b"infernoCTF123412"

iv = hashlib.md5(b"infernoCTF").digest()

# === Encrypt ===
cipher_encrypt = AES.new(key1, AES.MODE_CBC, iv=iv)
ciphertext = cipher_encrypt.encrypt(data)

# === Defeat weakenend keys by encrypting again ===
cipher_encrypt = AES.new(key2, AES.MODE_CBC, iv=iv)
ciphered_bytes = cipher_encrypt.encrypt(ciphertext)

print (base64.b64encode(ciphered_bytes))

test=base64.b64decode(b"TtIiVQmcmd/CvlMYA6ifDGAax72Pv6vuxTAsefTqYmMfxp/+wbgfzP6F+ayHvC0j")

aes = AES.new(key2, AES.MODE_CBC, iv)
decd = aes.decrypt(test)
aes = AES.new(key1, AES.MODE_CBC, iv)
print(aes.decrypt(decd))