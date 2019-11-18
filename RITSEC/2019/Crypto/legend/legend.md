# Legend

```
Hey Listen! Are you a legend?
Hint: you need to break a well known cipher!
Created By Security Risk Advisors for the RITSEC CTF
```

[! Spectrum Analysis with Audacity](audacity.png)

@ShiyamotoMigeru

https://twitter.com/ShiyamotoMigeru

At this point we had 2 cipher texts.

```
HEY! LISTEN!
d_ c` db dc cd ca ch c6 cb c7 c5 c6 bh da ba c2 cb bc ba
WDU3D3WISG33WTERKRCR3UEOTATDMHTR
```

As given in pre-legend, we knew we were going to use traspositioncypher at some point.

https://github.com/clayball/something-useful-ritsec/blob/master/transpositionDecrypt.py

First cipher text was not used at all which really confused me.

Modified the last part to see if we get something.
```
if __name__ == '__main__':
	for item in range(20):
		try:
			main(item)
		except ZeroDivisionError:
			pass
            ```
        
[! Decoded ](reddit.png)

https://www.reddit.com/user/TH3GR3ATD3KUTR33

```
t'vu#!L`vuoub!t#va#x#t{~_"{N
```

ROT47 + ROT13

[! Flag ](flag.png)


FLAG: RITSEC{1TS@S3CRET2EVERYB0DY}


