def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            offset = ord('A') if is_upper else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char

    return result

def encrypt():
    plaintext = input("plaintext: ")
    shift = int(input("what is the shift value? "))

    ciphertext = caesar_cipher(plaintext, shift)

    print("Encrypted Text:", ciphertext)

def decrypt():
    plaintext= input("text:")
    shift = int(input("shift value?"))

    ciphertext = caesar_cipher(plaintext, -shift)

    print("decrypted text:", ciphertext)

mode=input("what you want encrypt(1) or decrypt(2)?")
if mode == "1":
    encrypt()
elif mode == "2":
    decrypt()
else:
    print("incorrect input...")
