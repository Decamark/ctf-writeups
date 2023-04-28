According to [this](https://mudongliang.github.io/x86/html/file_module_x86_id_318.html) article:

```
Other than raising the invalid opcode exception, this instruction is the same as the NOP instruction.
```

# Disassembly

```
   0x55555555530b <main+170>    ud2    
 ► 0x55555555530d <main+172>    mov    rax, qword ptr [rbp - 0xb0]
   0x555555555314 <main+179>    add    rax, 8
   0x555555555318 <main+183>    mov    rax, qword ptr [rax]
   0x55555555531b <main+186>    mov    rdi, rax
   0x55555555531e <main+189>    call   strlen@plt                <strlen@plt>

   0x555555555323 <main+194>    cmp    rax, 0xc
   0x555555555327 <main+198>    jne    main+465                <main+465>

   0x55555555532d <main+204>    ud2    
   0x55555555532f <main+206>    mov    rax, qword ptr [rbp - 0xb0]
   0x555555555336 <main+213>    add    rax, 8
 ► 0x55555555533a <main+217>    mov    rax, qword ptr [rax]
   0x55555555533d <main+220>    mov    edx, 3
   0x555555555342 <main+225>    lea    rsi, [rip + 0xcd2]
   0x555555555349 <main+232>    mov    rdi, rax
 ► 0x55555555534c <main+235>    call   strncmp@plt                <strncmp@plt>
        s1: 0x7fffffffe39e ◂— 'AAAAAAAAAAAA'
        s2: 0x55555555601b ◂— 0x6e305f007a7449 /* 'Itz' */
        n: 0x3

 ► 0x55555555537c <main+283>    call   strncmp@plt                <strncmp@plt>
        s1: 0x7fffffffe3a1 ◂— 'AAAAAAAAA'
        s2: 0x55555555601f ◂— 0x5f794c006e305f /* '_0n' */
        n: 0x3

 ► 0x5555555553ac <main+331>    call   strncmp@plt                <strncmp@plt>
        s1: 0x7fffffffe3a4 ◂— 0x5800414141414141 /* 'AAAAAA' */
        s2: 0x555555556023 ◂— 0x324455005f794c /* 'Ly_' */
        n: 0x3

 ► 0x5555555553d8 <main+375>    call   strncmp@plt                <strncmp@plt>
        s1: 0x7fffffffe3a7 ◂— 0x5f47445800414141 /* 'AAA' */
        s2: 0x555555556027 ◂— 0x5448203e00324455 /* 'UD2' */
        n: 0x3
```
