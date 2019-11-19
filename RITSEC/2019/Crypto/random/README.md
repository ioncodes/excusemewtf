# random

We were given a netcat command: `nc ctfchallenges.ritsec.club 8001`. Connecting to it gives the following:

```
1281115560
1284535428
934066453
Are you starting to 'C' a pattern?
1575953984
663236232
Can you guess the next number?
```

The 5 numbers are always different and we have to guess the next number. I made a small binary that does `srand(time(0))` and then generates 6 values. You can find the file in `random.c`. Compile it using `gcc random.c -o random`. Run the file using `while true; do ./random; done > random.txt` and connect to the remote server. Now you can kill the `./random` process and look for the last value in the dump. Pick the value after that and submit it.

Flag: `RITSEC{404_RANDOMNESS_NOT_FOUND}`