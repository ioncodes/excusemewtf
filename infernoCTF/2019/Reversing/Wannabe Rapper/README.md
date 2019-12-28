# Wannabe Rapper

An Android Pentester and Wannabe Rapper extracted the following files from an app.

PS: He loves Eminem!!

flag : infernoCTF{username:password}

Author : MrT4ntr4


# Solution

For this challenge, we are given 3 smali files to extract username and password from.

### Username

For the username, one of the smali files contain the following:
```smali

.line 70
const-string v1, "m&m"

invoke-virtual {p1, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

move-result p1
```

The equality check on constant string and hint together give away that this is possibly the username.

### Password

For the password part, one of the methods point toward md5 (from its strings), and one of the methods is constucting a string array:
```
new-array v1, v1, [Ljava/lang/String;
```

And initializing that array as such:
```
const-string v2, "84"
const/4 v3, 0x0
aput-object v2, v1, v3
const-string v2, "5"
const/4 v3, 0x1
aput-object v2, v1, v3
const-string v2, "2"
const/4 v3, 0x2
aput-object v2, v1, v3
const-string v2, "f8eb53473"
aput-object v2, v1, v0
const-string v0, "4"
const/4 v2, 0x4
aput-object v0, v1, v2
const-string v0, "2efb3d"
const/4 v2, 0x5
aput-object v0, v1, v2
const-string v0, "f"
const/4 v2, 0x6
aput-object v0, v1, v2
const-string v0, "82df"
const/4 v2, 0x7
aput-object v0, v1, v2
```

So, from the part above, following object array is constructed:
`["84", "5", "2", "f8eb53473", "4", "2efb3d", "f", "82df"]`

Then, a join operation with "a" is executed on this array.
```
const-string v0, "a"
invoke-static {v0, v1}, Ljava/lang/String;->join(Ljava/lang/CharSequence;Ljava/lang/Iterable;)Ljava/lang/String;
```
So, "a".join(arr)

Our resulting string is `84a5a2af8eb53473a4a2efb3dafa82df`.

Then, every 8 is replaced with a 0 with the following part:
```
const-string v1, "8"
const-string v2, "0"
invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replaceAll(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
```

Then this value is stored as the "secret"
Our resulting hash is: `04a5a2af0eb53473a4a2efb3dafa02df`, which is easily cracked as `mockingbird78209`

Flag: `infernoCTF{m&m:mockingbird78209}`