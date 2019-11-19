# patch-2sday

We get two files: `patch-tuesday1` and `win32k.patched.sys`. The latter is actually not patched. A google search for the version and a quick md5 on it reveals that. So what's the other file?

```
$ strings patch-tuesday1
PA30
jG}D
```

The `PA30` string looks very interesting. After a while of googling we figure out there's DLLs in Windows called `mspatcha.dll` and `mspatchc.dll`. These are unfortunately outdated and work for `PA19`. Googling more reveals there's a new DLL called `msdelta.dll`. I actually found it by googling and figuring out it's a delta format and just searching for any `*delta*.dll` files. Interfacing with the DLL wasn't an easy task as there's barely any resources on it. I made a Python script and a C# solution for this. In this repo you will find the Python script (`delta_patcher.py`) as it was the last thing I was working with. It didn't work perfectly as I would have expected but later on I figured out that the first 4 bytes are a CRC checksum which had to be removed. With the new `win32k.actually.patched.sys` we can now get the flag. let's diff the original file and the patched file:

```
xxd win32k.patched.sys > 1.hex
xxd win32k.actually.patched.sys > 2.hex
diff 1.hex 2.hex
```

Flag: `RITSEC{NOSERIOUSLYPATCHME}`