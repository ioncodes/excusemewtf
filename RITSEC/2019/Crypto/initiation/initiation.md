# Initiation - 300 Points

## Challenge

The final flag is in english and must be wrapped in RITSEC{ }

Attached Image:  [secret](secret.png)

Attached Image:  [hint](hint.jpg)

## Solution

![secret](secret.png) 

We are given an encrypted flag, containing several unknown symbols and a map of europe with a character from magic the gathering on top, the simic manipulator. The map shows europe in the 18th century so we are looking for a historic cipher. It turns out to be the copiale cipher which can be translated by hand via several lookup tables online (for example this one: [Copiale](http://kryptografie.de/kryptografie/chiffre/images/copiale.png)).

This gives the string: "gruselige kulte und alte chiffren". Since the flag is in english we have to translate it.

RITSEC{scary cults and old ciphers}