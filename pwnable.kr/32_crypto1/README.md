# crypto1
AES128 CBC mode splits an original plaintext into 16 bytes long blocks and encrypts each.

The format of a plaintext is `{id}-{pw}-{cookie}`. Given `'a'*13` as `id` and null as `pw`, the plaintext would be `aaaaaaaaaaaaa` + `-` + `-` + `{cookie}`. Its first block is `aaaaaaaaaaaaa--{x}` where `x` is the first character of the cookie. The corresponding ciphertext is `87b47bf98c9fb06902e11d763c09c7ab`.

| id | pw |
| --- | --- |
| `aaaaaaaaaaaaa` | `-{y}` |

This constructs `aaaaaaaaaaaaa--{y}-{cookie}` and we can find `x` by brute-forcing `y` and comparing its ciphertext with the above one. How can we get the second character of the cookie? We just need to decrease the number of `a` by one, append `y` and brute-force `z`: `aaaaaaaaaaaa--{y}{z}`. This procedure gives us the first 14 bytes of the cookie (We can obtain the 14th when `'a'` becomes null).

The main idea is same of the 15th and later: Adjust the length of known characters 15 mod 16. For example, the 15th can be obtained via `aaaaaaaaaaaaaaa--you_will_never{x}`.

## References
* https://github.com/victor-li/pwnable.kr-write-ups/blob/master/crypto1.md
* https://aquaorinfosec.tistory.com/83
