import random

def isPrime(element):
    for i in range (2,element):
        if element%i==0:
            return False
    return True

def isPrimitiveRoot(element, i):
    values = []
    for j in range (1,element):
        if pow(i,j,element) in values:
            return False
        else:
            values.append(pow(i,j,element))
    return True

def GCD(a,b):
    factors_a = set()
    factors_b = set()

    for i in range (2,a+1):
        if a%i==0:
            factors_a.add(i)
    for i in range (2,b+1):
        if b%i==0:
            factors_b.add(i)
    L = factors_a.intersection(factors_b)
    if len(L)==0:
        return True
    else:
        return False
    
def inverse(element,p):
    for i in range (1,element):
        if element*i%p==1:
            return i
    return -1

while (True):
    print("Enter p (prime number) : ")
    p = int(input())
    if isPrime(p):
        break
    else:
        print("Please enter a prime number !")

#Generating Private-Public Key Pairs
primitive_roots = []
for i in range (1,p):
    if isPrimitiveRoot(p,i):
        primitive_roots.append(i)

g = random.choice(primitive_roots)

x_a = random.randrange(2,p-2)
y_a = pow(g,x_a,p)

print("Alice's Private Key : ",x_a)
print("Alice's Public Key : ",y_a)

print("Enter the message : ")
m = int(input())

h_m = m%256

#Generating a Digital Signature
while (True):
    k = random.randrange(2,p-2)
    if GCD(k,p-1):
        break

s1 = pow(g,k,p)
inverse_k = inverse(k,p-1)
s2 = (inverse_k*(h_m-x_a*s1))%(p-1)

print("Signature (s1,s2) : ",(s1,s2))

#Verifying Signature

v1 = pow(g,h_m,p)
v2 = pow(y_a,s1)*pow(s1,s2)%p

if (v1==v2):
    print("Signature is valid !")
else:
    print("Signature is invalid !")