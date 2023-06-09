from pwn import *
from pwnlib.asm import *

arm1   = b"\x01\x60\x8f\xe2\x16\xff\x2f\xe1"
thumb1 = b"\x01\xb5\x92\x1a\x10\x1c\xf0\x46\x02\x4a\x90\x47"
thumb2   = b"\x02\x4a\x1c\x32\x90\x47\x01\xbd\x24\xf9\x03\x80\x50\xf5\x03\x80"

print( disasm(arm1, arch='arm') )
print( disasm(thumb1, arch='thumb') )
print( disasm(thumb2, arch='thumb') )
