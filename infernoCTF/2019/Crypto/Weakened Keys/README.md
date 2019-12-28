# Weakened Keys
## 400

Local politicians and their anti crypto opinions have forced us to dumb down our AES encryption. It's OK because we think we can still use these weakened keys and still encrypt our message securely by encrypting it twice. Have a look at our code and see what you think.

Encrypted Test= '0mu0T97looX5/Oorw8ASGxfqMqrNoFajZupXrjtIAj7ECJdQXZzEmbEwdRV2J2MI' Test = 'Double AES encryption for twice the strength.Win'

flag = 'lIZMVkA+pbiOxh3nNdV2bWz3gXovIy4fG7yCHa5FT44='

Author : alphachaos

file: `doubleAes.py`



# Solution

With this challenge, we are given a flag double-aes encrypted with two diferent keys. Lucky for us, we also have a ciphertext that we have the plaintext for, which used the same keys.

To attack this, we can "make the plain and cipher meet in the middle". So we can generate key after key, and encrypt the plaintext, and decrypt the ciphertext while saving every result on seperate tables.

If there is a common middleman, it means we know both key1 and key2 or the cipher.


Incremental key generation i always use (modified to match the padding):

```py
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
	###do stuff##
```

After encrypting and decrypting with each key, i wrote all the results (b64 encoded) to seperate files, and used:
```bash
awk 'NR==FNR{arr[$0];next} $0 in arr' enc.txt dec.txt
```
to find the middleman.

After finding the middleman, key can be regenerated from the line number of each file where middleman was found.

**Complete script for finding the middleman is `middleman.py`**

So keys are:
```py
key1 = "0000000000000000000000000000021Q"
key2 = "00000000000000000000000000000(iA"
```

Then, we can verify the keys and then decrypt the flag using the script in `solveWK.py`


Flag: `infernoCTF{M33t_in_Th£_M1ddL3!}`
