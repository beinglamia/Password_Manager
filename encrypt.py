
def encrypt(string):
    cipher_text=" ".join(format(ord(c),'b') for c in string)
    return cipher_text

# print(encrypt(message))
def decrypt(cipher_text):
    list=cipher_text.split()
    plain_text=''
    for c in list:
        plain_text+= chr(int(c,2))
    return plain_text





if __name__=='__main__':
    message="Hello World "
    # encyt=encrypt(message)
    # print(encyt)
    # decy=decrypt(encyt)
    # print(decy)
    s='1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100 100000'
    print(decrypt(s))
