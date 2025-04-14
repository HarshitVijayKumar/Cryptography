import random

def isPrime(element):
    for i in range (2,element):
        if element%i==0:
            return False
    return True

def findInverse(k, q):
    for i in range (1,q):
        if k*i%q==1:
            return i
    return -1


#Key Generation
while (True):
    print("Enter the value of p : ")
    p = int(input())
    if isPrime(p):
        break
    print("Please enter a prime number !")

divisors = []
for i in range (2,p):
    if (p-1)%i==0:
        if isPrime(i):
            divisors.append(i)
q = random.choice(divisors)

while (True):
    h = random.randint(2,p-2)
    if pow(h,int((p-1)/q),p)>1:
        break

g = pow(h,int((p-1)/q),p)
x = random.randint(1,q-1)
y = pow(g,x,p)
print("Public Key : (p,q,g,y)", (p,q,g,y))


print("Enter the message : ")
m = int(input())

H_m = m%26

#Signature Generation
k = random.randint(1,q-1)
k_inverse = findInverse(k,q)
r = (pow(g,k)%p)%q
s = (k_inverse*(H_m + x*r))%q
print("Digital Signature : (r,s) ",r,s)

#Signature Verification
if (r<=0) or (r>=q) or (s<=0) or (s>=q):
    print("Invalid Signature !")
else:
    s_inverse = findInverse(s,q)
    w = s_inverse%q
    u1 = (H_m*w)%q
    u2 = (r*w)%q
    v = (pow(g,u1)*pow(y,u2)%p)%q
    if (v==r):
        print("Valid Signature ! ")
    else:
        print("Invalid Signature ! ")