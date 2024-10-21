from cryptography.fernet import Fernet
#key = Fernet.generate_key()

mykey = b'pTO_ZUFlUKBITx82O7phbAR0u0oyrdqjPAnPJv6dkx8='


def encrypt(plaintext):
    f = Fernet(mykey)
    #print(type(f.encrypt(plaintext)))
    textbytes = bytes(plaintext, 'utf-8')
    return f.encrypt(textbytes)

def decrypt(ciphertext):
    f = Fernet(mykey)
    textbytes = f.decrypt(ciphertext)
    return str(textbytes, encoding='utf-8')
    

# if __name__ == '__main__':
#     print(type(encrypt('Hello')))
#     result = (encrypt('Hello'))
#     print(decrypt(result))
