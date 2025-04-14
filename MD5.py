import math

def dec_to_bin(element):
    output = bin(int(element))
    new_output = output[2:]
    while (len(new_output)<32):
        new_output = "0"+new_output
    return new_output

def bin_to_dec(element):
    output = 0
    mult = 1
    for i in range (len(element)-1,-1,-1):
        if element[i]=='1':
            output += mult
        mult = mult*2
    return output

def hex_to_bin(element):
    output = ""
    d = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
    }
    for i in element:
        output += d[i]
    return output

def bin_to_hex(element):
    output = ""
    d = {
        "0000":"0",
        "0001":"1",
        "0010":"2",
        "0011":"3",
        "0100":"4",
        "0101":"5",
        "0110":"6",
        "0111":"7",
        "1000":"8",
        "1001":"9",
        "1010":"A",
        "1011":"B",
        "1100":"C",
        "1101":"D",
        "1110":"E",
        "1111":"F"
    }
    for i in range (0,len(element),4):
        output += d[element[i]+element[i+1]+element[i+2]+element[i+3]]
    return output

def AND(a,b):
    output = ""
    for i in range (0,len(a)):
        if (a[i]=="1")and(b[i]=="1"):
            output += "1"
        else:
            output += "0"
    return output

def OR(a,b):
    output = ""
    for i in range (0,len(a)):
        if (a[i]=="0")and(b[i]=="0"):
            output += "0"
        else:
            output += "1"
    return output

def XOR(a,b):
    output = ""
    for i in range (0,len(a)):
        if (a[i]==b[i]):
            output += "1"
        else:
            output += "0"
    return output

def NOT(a):
    output = ""
    for i in range (0,len(a)):
        if a[i]=="0":
            output += "1"
        else:
            output += "0"
    return output

def F(B,C,D):
    output = ""
    d = {"1":1,"0":0}
    e = {1:"1", 0:"0"}
    for i in range (0,len(B)):
        output += e[(d[B[i]]&d[C[i]])|(~d[B[i]]&d[D[i]])]
    return output

def left_rotate(element, shifts):
    output = element[shifts:]
    output += element[:shifts]
    return output


rotate_by = [7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22]

print("Enter the message (in hexadecimal) : ")
message = input()

#Insert Padding Bits
length = len(message)

i = 1
while (512*i-64<4*length):
    i += 1

padding_bits = 512*i-64-4*length
new_message = hex_to_bin(message)
new_message += "1"
for _ in range (1,padding_bits):
    new_message += "0"

#Append length bits
new_message += dec_to_bin(4*length)
message = new_message

#Initialise MD buffer
A = "01234567"
B = "89ABCDEF"
C = "FEDCBA98"
D = "76543210"

#Process each block
k = []
for i in range (0,64):
    a = abs(math.sin(i+1))*(pow(2,32))
    k.append(dec_to_bin(a))

a = hex_to_bin(A)
b=  hex_to_bin(B)
c = hex_to_bin(C)
d = hex_to_bin(D)
s = 0

for i in range (0,len(message),32):
    block = message[i:i+32]
    for j in range (0,64):
        t = bin_to_dec(F(b,c,d))
        t = (t+bin_to_dec(a))%pow(2,32)
        t = (t+bin_to_dec(block))%pow(2,32)
        t = (t+bin_to_dec(k[j]))%pow(2,32)
        new_t = left_rotate(dec_to_bin(t),rotate_by[s])
        t = (bin_to_dec(new_t)+bin_to_dec(b))%pow(2,32)
        a = d
        b = dec_to_bin(t)
        c = b
        d = c
    s += 1

print("Resultant Hash : ")
print(bin_to_hex(a)+bin_to_hex(b)+bin_to_hex(c)+bin_to_hex(d))
