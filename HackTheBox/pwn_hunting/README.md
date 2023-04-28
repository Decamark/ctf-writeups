# 0x56556460

```c
strcpy(local_18, "HTB{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}");
memset(EBX+0x78, 0, 0x25);

prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0);

mmap;
read;
();
```

At the end of this function, we can execute any shellcode.
This program seems to be injected the flag externally.
Shellcode that explores its memory will find the flag as [this article](https://shakuganz.com/2021/07/14/hackthebox-hunting-write-up/) says. Note that Each page is 4096 bytes-long in VAS and we can skip to the next page when EFAULT occurs.

# See also

* [Paging in Virtual Memory](https://compas.cs.stonybrook.edu/~nhonarmand/courses/fa17/cse306/slides/06-paging.pdf)
