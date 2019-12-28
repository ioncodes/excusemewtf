# Check Again
## 200

Did you check the site , I mean check again.

Hint: `Dante Nero Sparda are the true demons.`

# Solution

After seeing the hint, Dante Nero Sparda obviously points towards the DNS.

Half of the flag is from the TXT records of the ctf website.

```
kali@kali:~$ dig TXT infernoCTF.live

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> TXT infernoCTF.live
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 9898
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;infernoCTF.live.		IN	TXT

;; ANSWER SECTION:
infernoCTF.live.	300	IN	TXT	"ca3-d0f129e83e07442d981e6eadd9e57915"
infernoCTF.live.	300	IN	TXT	"70_h1d3_1n_th3_Rec0rds}"

;; Query time: 207 msec
;; SERVER: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
;; WHEN: Sat Dec 28 11:05:19 EST 2019
;; MSG SIZE  rcvd: 129
```


Other and first half is from the spf records for the domain.

```
kali@kali:~$ dig SPF infernoCTF.live

; <<>> DiG 9.11.5-P4-5.1+b1-Debian <<>> SPF infernoCTF.live
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44561
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;infernoCTF.live.		IN	SPF

;; ANSWER SECTION:
infernoCTF.live.	300	IN	SPF	"v=spf1 a mx ?all - infernoCTF{N1c3_Pl4c3_"

;; Query time: 258 msec
;; SERVER: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
;; WHEN: Sat Dec 28 11:06:40 EST 2019
;; MSG SIZE  rcvd: 98
```

flag: `infernoCTF{N1c3_Pl4c3_70_h1d3_1n_th3_Rec0rds}`