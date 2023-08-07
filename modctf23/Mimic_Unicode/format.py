from binascii import *

mimic = open('mimic.txt', 'br')
clear = open('clear.txt', 'bw')

while True:
        clear.write( hexlify(mimic.read(1)) )
        clear.write( hexlify(mimic.read(1)) )
        clear.write( hexlify(mimic.read(1)) )

        clear.write( b'\n' )
