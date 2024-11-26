* PR_SET_NO_NEW_PRIVS (38, 0x26) - 1
* PR_SET_SECCOMP (22, 0x16) - 2 SECCOMP_MODE_FILTER

# Securities

```
seccomp-tools dump ./gachi-rop 
 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x05 0xc000003e  if (A != ARCH_X86_64) goto 0007
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x03 0x00 0x40000000  if (A >= 0x40000000) goto 0007
 0004: 0x15 0x02 0x00 0x0000003b  if (A == execve) goto 0007
 0005: 0x15 0x01 0x00 0x00000142  if (A == execveat) goto 0007
 0006: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0007: 0x06 0x00 0x00 0x00050000  return ERRNO(0)
```

Also, NX bit is set.

# Solution
* vmmap - DATA section
ropr might be helpful

```
ropr libc.so.6 -m 3 | grep -E "mov \[r[b-z]x\], rax"
```
