from base64 import b64decode

encoded = "cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA=="
decoded = b64decode(encoded)

original = [0] * 0x40

key = b"FlareOn2024"

for i in reversed(range(0, 0x40)):
    j = ((0x5d1745d1745d1746 * i) & 0xff0000000000000000)
    j = j >> 8*8
    j = j >> 2
    j = j * 0xb
    j = i - j

    original[i] = decoded[i] ^ key[j]

print(bytes(original).decode('utf-8'))
