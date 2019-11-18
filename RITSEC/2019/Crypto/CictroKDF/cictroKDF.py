from Crypto.Cipher import AES
import base64

def check(word):
    return len(word) % 4 == 0

def calc(msg):
    state = ['h','a','s','h']
    for i in range(len(msg)):
        state[i%4] = round(ord(msg[i]),i)
    return expand(state)


def round(b,i):
    global state
    a = b
    for k in range(100):
        a = om(pi(a,k),b)
    return a

def phi(b,k):
    return om(pi(b,k),b)

def om(x,y):
    return x ^ y ^ 56

def pi(n, k):
    bi = list(map(int, list(bin(n)[2:].zfill(8))))
    nbi = [0,0,0,0,0,0,0,0]
    bi[7-(k%8)] = 1
    nbi[3] = bi[0]
    nbi[4] = bi[1] ^ bi[0]
    nbi[6] = bi[2] ^ bi[5]
    nbi[7] = bi[3]
    nbi[1] = bi[4]
    nbi[0] = bi[5]
    nbi[5] = bi[6]
    nbi[2] = bi[7] ^ bi[5]

    return int(''.join([str(x) for x in nbi]),2)

def exp(w,l):
    return pi(w[0]^w[1]^w[l-1]^w[l],101)

def expand(state):
    out = state
    while len(out) < 19:
        out.append(exp(out,len(out)-1))
    return out[3:]

message = "Are you silly? I'm still gunna send it!!"
#message = "it!!"
assert check(message)
out = calc(message)
key =''.join([chr(x) for x in out])
cipher = AES.new(key,AES.MODE_ECB)
ct = base64.b64decode('E2zVOQfaRwYoMiTapzA03RQJJmtq1KuHTCuWGdVo/+w=')
pt = cipher.decrypt(ct)

print "key: "+key
print "plaintext: "+pt
print "Flag: RITSEC{"+pt+"}"
