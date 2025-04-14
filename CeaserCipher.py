print("Enter the plaintext: ")
p = input()
print("Enter the key: ")
k = int(input())

print("Encrypting .....")
c = ""
for i in p:
    if ord(i)>96 and ord(i)<123:
        c += chr(((ord(i)-97+k)%26)+97)
    elif ord(i)>64 and ord(i)<91:
        c += chr(((ord(i)-65+k)%26)+65)
    else:
        c += i
print(c)

print("Decrypting .....")
d = ""
for i in c:
    if ord(i)>96 and ord(i)<123:
        d += chr(((ord(i)-97-k)%26)+97)
    elif ord(i)>64 and ord(i)<91:
        d += chr(((ord(i)-65-k)%26)+65)
    else:
        d += i
print(d)