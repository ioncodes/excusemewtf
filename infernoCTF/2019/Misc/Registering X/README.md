# Registering X
## 300

Do you have your ex's registered?

Author: SVM

file:`chal.txt`

# Solution

chal.txt that is given to us contains the following:
```
Here's a regex 4 u. Match it if you can...

infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}(?<=\s)g_fUn\W(?<=[A-z])}(?<=\..{14})(?<=^.{33})
```

So we just need to generate a flag that matches this regex.

To solve this, my strategy was starting from left to right, and cascading regex's in small chunks and making sure the flag i have so far matches the regex.


### Starting generation
Well, first part is pretty obvious.

```
regex: infernoCTF{

flag:  infernoCTF{
```

---

`.(?<=H).` Means anything that is not preceeded by `H`

```
regex: infernoCTF{.(?<=H){21}.

flag:  infernoCTF{H?
```

---

`[a-z](?<=\+a)` means anything a-z is preceeded by +a

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}

flag:  infernoCTF{H+a
```

---
`[a-z][a-j]` is to characters in those respective ranges, lets give them both "j" values.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j]

flag:  infernoCTF{H+ajj
```

---
`(?<!([a-u]|[w-z])(j|[a-h]))` is a character that is not preceeded by a-u, w-z, followed by "j" or something in range a-h

For the part that will follow, lets pick "e" from `(j|[a-h])`.

We have to modify the last part we added, "jj" to end with e, and first part to not be in range of a-u \| w-z

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h]))

flag:  infernoCTF{H+ave
```

---
`.{2,64}` is any string with a length of 2 to 64, lets keep it short and say its 2 for now.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}

flag:  infernoCTF{H+ave??
```

---
`(?<!\S){255}n` is an "n" not preceeded by `\S`. \S is any non-whitespace character. So this means space, then "n".

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n

flag:  infernoCTF{H+ave?? n
```

---
`.{2}` is random 2 length string, easy enough.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}

flag:  infernoCTF{H+ave?? n??
```

---
`(?<=\s)g_fUn` is g_fUn, preceeded by \s, which means a whitespace character. We can change one of the wildcards to space now, and add the literal phrase.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}(?<=\s)g_fUn

flag:  infernoCTF{H+ave?? n? g_fUn
```

---
`\W` is "any non-word character", and will match `[^a-zA-Z0-9_]`.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}(?<=\s)g_fUn\W

flag:  infernoCTF{H+ave?? n? g_fUn  (whitespace at the end)
```

---
`(?<=[A-z])}` is "}" not preceeded by A-z. We can change the whitespace we used for \W to "[", which will be in A-z range, and will be matched by \W.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}(?<=\s)g_fUn\W(?<=[A-z])}

flag:  infernoCTF{H+ave?? n? g_fUn[}
```

---
`(?<=\..{14})` means we had a literal dot character 14 characters ago. We can fix that by making sure its in the range of .{2,64} and setting that character to "."

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}(?<=\s)g_fUn\W(?<=[A-z])}(?<=\..{14})

flag:  infernoCTF{H+ave.??? n? g_fUn[}
```

---
`(?<=^.{33})` means special string starts operator was 33 characters ago, and our flag is 32 characters long. We can archieve this by padding the .{2,64} part, before the dot, until we reach the correct length.

```
regex: infernoCTF{.(?<=H){21}.[a-z](?<=\+a){1024}[a-z][a-j](?<!([a-u]|[w-z])(j|[a-h])).{2,64}(?<!\S){255}n.{2}(?<=\s)g_fUn\W(?<=[A-z])}(?<=\..{14})(?<=^.{33})

flag:  infernoCTF{H+ave??.??? n? g_fUn[}
```


Flag (kind of): `infernoCTF{H+ave??.??? n? g_fUn[}`






