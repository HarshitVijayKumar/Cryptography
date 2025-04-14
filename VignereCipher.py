print("Enter the key : ")
key = input()
key = key.upper()

print("Enter the plaintext : ")
plaintext = input()
plaintext = plaintext.upper()

while (len(key)<len(plaintext)):
    key += key

#Encryption
ciphertext = ""
for i in range (0,len(plaintext)):
    ciphertext += chr((((ord(plaintext[i])-65)+(ord(key[i])-65))%26)+65)

print("Encrpytion ... ")
print(ciphertext)

#Decrpytion
plaintext = ""
for i in range (0,len(ciphertext)):
    plaintext += chr((((ord(ciphertext[i])-65)-(ord(key[i])-65))%26)+65)

print("Decyption ... ")
print(plaintext)