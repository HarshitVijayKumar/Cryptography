print("Enter the plaintext : ")
p = input()
p = p.upper()

print("Enter the value of N for the key : ")
n = int(input())

key = []
print("Enter the key")
for i in range (0,n):
    L = []
    for j in range (0,n):
        a = int(input())
        L.append(a)
    key.append(L)

encryption = ""
for i in range (0,len(p)//n):
    w = []
    for j in range (i*n,i*n+n):
        w.append(ord(p[j])-65)
    e = []
    for j in range (0,n):
        a = 0
        for k in range (0,n):
            a += key[j][k]*w[k]
        e.append(chr(a%26+65))
    encryption += "".join(e)

print("Encrypted Word is : ")
print(encryption)