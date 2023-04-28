from pwnlib.asm import *

print( disasm(b'\x78\x46\x0e\x30', arch='thumb') )
