print("Enter the plaintext: ")
p = input()
p = p.upper()
print("Enter the key: ")
k = input()
k = k.upper()

k_new = ""
for i in k:
    if i not in k_new:
        k_new += i
k = k_new

alphabets = []
for i in range (0,26):
    alphabets.append(chr(65+i))
alphabets.remove('J')
matrix = []

for i in range (0,5):
    L = []
    for j in range (0,5):
        if 5*i+j<len(k):
            if k[5*i+j] not in alphabets:
                continue
            if k[5*i+j]=='J':
                L.append('I')
                alphabets.remove('I')
            else:
                L.append(k[5*i+j])
                alphabets.remove(k[5*i+j])
        else:
            element = alphabets.pop(0)
            L.append(element)
    matrix.append(L)

if len(p)%2!=0:
    p += 'Z'

c = ""

i = 0
while (i<len(p)):
    a = p[i]
    i += 1
    b = p[i]
    i += 1

    a_row = -1
    a_col = -1
    b_row = -1
    b_col = -1
    i_row = -1
    i_col = 5

    for j in range (0,5):
        for k in range (0,5):
            if matrix[j][k]==a:
                a_row = j
                a_col = k
            elif matrix[j][k]==b:
                b_row = j
                b_col = k
            elif matrix[j][k]=='I':
                i_row = j
                i_col = k
    if a=='J':
        a_row = i_row
        a_col = i_col
    if b=='J':
        b_row = i_row
        b_col = i_col
    if a_row==b_row:
        c += matrix[a_row][(a_col+1)%5]
        c += matrix[b_row][(b_col+1)%5]
    elif a_col==b_col:
        c += matrix[(a_row+1)%5][a_col]
        c += matrix[(b_row+1)%5][b_col]
    elif a_row==b_row and a_col==b_col:
        c += matrix[a_row][a_col]
        c += 'x'
        c += matrix[a_row][a_col]
    else:
        c += matrix[b_row][a_col]
        c += matrix[a_row][b_col]

print("Encryption .....")
print(c)