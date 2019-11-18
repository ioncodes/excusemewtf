import base64

data = open('onionlayerencoding.txt').read()
flag = ''

for x in range(32):
    try:
        flag=base64.b16decode(data)
        data=flag
        continue
    except:
        pass
    try:
        flag=base64.b32decode(data)
        data=flag
        continue
    except:
        pass
    try:
        flag=base64.b64decode(data)
        data=flag
        continue
    except:
        pass
print flag
