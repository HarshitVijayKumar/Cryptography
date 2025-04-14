def GCD(a,b):
    a_factors = set()
    b_factors = set()
    for i in range (1,a):
        if a%i==0:
            a_factors.add(i)
    for i in range (1,b):
        if b%i==0:
            b_factors.add(i)
    common_divisors = a_factors.intersection(b_factors)
    if len(common_divisors)==1:
        return True
    return False

def isPrime(a):
    a_factors = set()
    for i in range (1,a):
        if a%i==0:
            a_factors.add(i)
    if len(a_factors)==1:
        return True
    return False

while True:
    print("Enter p : ")
    p = int(input())
    print("Enter q : ")
    q = int(input())

    if not isPrime(p) or p<3:
        print("Please enter a valid prime number for p")
    elif not isPrime(q) or q<3:
        print("Please enter a valid prime number for q")
    else:
        break

n = p*q
phi_n = (p-1)*(q-1)

avoid = []
while True:
    for e in range (3,phi_n):
        if GCD(e,phi_n) and e not in avoid:
            avoid.append(e)
            break
    print("e is calculated to be :",e)

    #Finding d
    for d in range (1, phi_n):
        if (d*e)%phi_n==1:
            break
    print("Private key is :",d)
    if d != phi_n-1:
        break

#Encrypting 
#C = M^e mod n
while True:
    print("Enter M : ")
    M = int(input())
    if M>n:
        print("Please enter an M value less than or equal to : ", n)
    else:
        break
C = pow(M,e)%n
print("Encryption :", C)

#Decrpyting
#M = C^d mod n
M = pow(C,d)%n
print("Decryption :",M)

#devipriya.av@vit.ac.in