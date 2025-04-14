import math
p = 23 #Prime Number
g = 5 #Primitive Root
a = 6 #Alice's Private Key
b = 15 #Bob's Private Key
e = 10 #Eve's Private Key

#Alice's public key
public_a = pow(g,a,p)

#Bob's public key
public_b = pow(g,b,p)

#Eve's public key
public_e = pow(g,e,p)

#Interception
K_a = pow(public_e,a,p) #Alice derives
K_b = pow(public_e,b,p) #Bob derives

#Eve derives
K_e_A = pow(public_a,e,p)
K_e_B = pow(public_b,e,p)

#All the keys
print("Alice's ---\n")
print("Private Key : ", a)
print("Public Key : ", public_a)
print("Derived Public Key from Bob : ", K_a)

print("Bob's ---\n")
print("Private Key : ", b)
print("Public Key : ",public_b)
print("Derived public key from Alice : ", K_b)

print("Eve's ---\n")
print("Private Key : ", e)
print("Public Key : ", public_e)
print("Derived from Alice : ", K_e_A)
print("Derived from Bob : ", K_e_B)