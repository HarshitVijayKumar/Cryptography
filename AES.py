def hex2bin(element):
    output = ""
    d = {
        '0':"0000",
        '1':"0001",
        '2':"0010",
        '3':"0011",
        '4':"0100",
        '5':"0101",
        '6':"0110",
        '7':"0111",
        '8':"1000",
        '9':"1001",
        'A':"1010",
        'B':"1011",
        'C':"1100",
        'D':"1101",
        'E':"1110",
        'F':"1111",
    }
    for i in range (0,len(element)):
        output += d[element[i]]
    return output

def bin2hex(element):
    output = ""
    d = {
        "0000":'0',
        "0001":'1',
        "0010":'2',
        "0011":'3',
        "0100":'4',
        "0101":'5',
        "0110":'6',
        "0111":'7',
        "1000":'8',
        "1001":'9',
        "1010":'A',
        "1011":'B',
        "1100":'C',
        "1101":'D',
        "1110":'E',
        "1111":'F',
    }
    for i in range (0,len(element),4):
        a = element[i]+element[i+1]+element[i+2]+element[i+3]
        output += d[a]
    return output

def hex2dec(element):
    d = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }
    row = element[0]
    col = element[1]
    return d[row], d[col]

def xor(a,b):
    output = ""
    for i in range (0,len(a)):
        if a[i]==b[i]:
            output += "0"
        else:
            output += "1"
    return output

def left_shift(element,shifts):
    new_element = element[shifts:]
    new_element += element[:shifts]
    return new_element

s_box = [
    "63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76",
    "CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0",
    "B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15",
    "04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75",
    "09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84",
    "53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF",
    "D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8",
    "51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2",
    "CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73",
    "60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB",
    "E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79",
    "E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08",
    "BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A",
    "70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E",
    "E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF",
    "8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"
]

inv_s_box = [
    "52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB",
    "7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB",
    "54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E",
    "08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25",
    "72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92",
    "6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84",
    "90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06",
    "D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B",
    "3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73",
    "96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E",
    "47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B",
    "FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4",
    "1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F",
    "60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF",
    "A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61",
    "17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D",
]

predefine_matrix = [[2,3,1,1],
                    [1,2,3,1],
                    [1,1,2,3],
                    [3,1,1,2]]

rconf = ["01000000","02000000","03000000","04000000","08000000","10000000","20000000","40000000","80000000","1B000000","36000000"]

key = b'Thats my Kung Fu'
plaintext = b'Two One Nine Two'

#Key_Expansion

keys = [key.hex().upper()]

for i in range (0,10):
    w0 = keys[-1][:8]
    w1 = keys[-1][8:16]
    w2 = keys[-1][16:24]
    w3 = keys[-1][24:]

    new_w3 = left_shift(w3,1)
    output = ""
    for j in range (0,len(w3),2):
        element = w3[j]+w3[j+1]
        row, col = hex2dec(element)
        output += s_box[row*16+col]
    new_output = bin2hex(xor(hex2bin(output),hex2bin(rconf[i])))
    
    w4 = bin2hex(xor(hex2bin(w0),hex2bin(new_output)))
    w5 = bin2hex(xor(hex2bin(w1),hex2bin(w4)))
    w6 = bin2hex(xor(hex2bin(w2),hex2bin(w5)))
    w7 = bin2hex(xor(hex2bin(w3),hex2bin(w6)))

    keys.append(w4+w5+w6+w7)

#Inital Message 
message = plaintext.hex().upper()

#Add Round Key
message = bin2hex(xor(hex2bin(message),hex2bin(keys[0])))

#Rounds 1-9

for i in range (1,10):
    output = ""
    for j in range (0,len(message),2):
        row,col = hex2dec(message[j]+message[j+1])
        output += s_box[row*16+col]
    new_output = output[:8]+bin2hex(left_shift(hex2bin(output[8:16]),1))+bin2hex(left_shift(hex2bin(output[16:24]),2))+bin2hex(left_shift(hex2bin(output[24:]),3))
    matrix = []
    for j in range (0,len(new_output),2):
        a,b = hex2dec(new_output[j]+new_output[j+1])
        matrix.append(16*a+b)

    new_matrix = []
    for s in range (0,4):
        L = []
        for d in range (0,4):
            L.append(matrix[s*4+d])
        new_matrix.append(L)
    
    #Mix Columns 
    matrix = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    
    for s in range (0,4):
        for d in range (0,4):
            new_element = (predefine_matrix[s][0]*new_matrix[0][d])%256
            for f in range (1,4):
                new_element ^= (predefine_matrix[s][f]*new_matrix[f][d])%256
            matrix[s][d] = hex(new_element)
            if len(matrix[s][d]) == 3:
                matrix[s][d] = '0x0'+matrix[s][d][2:]
    
    output = ""
    for s in range (0,4):
        for d in range (0,4):
            output += matrix[s][d].upper()[2:]
    message = bin2hex(xor(hex2bin(output),hex2bin(keys[i])))

#Round 10

output = ""
for j in range (0,len(message),2):
    row,col = hex2dec(message[j]+message[j+1])
    output += s_box[row*16+col]
new_output = output[:8]+bin2hex(left_shift(hex2bin(output[8:16]),1))+bin2hex(left_shift(hex2bin(output[16:24]),2))+bin2hex(left_shift(hex2bin(output[24:]),3))
matrix = []
for j in range (0,len(new_output),2):
    a,b = hex2dec(new_output[j]+new_output[j+1])
    matrix.append(hex(16*a+b).upper())
    if len(matrix[-1])==3:
        matrix[-1] = '0x0'+matrix[-1][2:]
output = ""
for i in range (0,len(matrix)):
    output += matrix[i][2:]

message = bin2hex(xor(hex2bin(output),hex2bin(keys[10])))
print(message)