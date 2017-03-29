def init():

    pc1 = [56, 48, 40, 32, 24, 16,  8,
            0, 57, 49, 41, 33, 25, 17,
            9,  1, 58, 50, 42, 34, 26,
	    18, 10,  2, 59, 51, 43, 35,
	    62, 54, 46, 38, 30, 22, 14,
	    6, 61, 53, 45, 37, 29, 21,
	    13,  5, 60, 52, 44, 36, 28,
	    20, 12,  4, 27, 19, 11,  3
	]

    pc2 = [ 13, 16, 10, 23,  0,  4,
	    2, 27, 14,  5, 20,  9,
	    22, 18, 11,  3, 25,  7,
	    15,  6, 26, 19, 12,  1,
	    40, 51, 30, 36, 46, 54,
	    29, 39, 50, 44, 32, 47,
	    43, 48, 38, 55, 33, 52,
	    45, 41, 49, 35, 28, 31
	]

    ip = [  57, 49, 41, 33, 25, 17, 9,  1,
            59, 51, 43, 35, 27, 19, 11, 3,
	    61, 53, 45, 37, 29, 21, 13, 5,
	    63, 55, 47, 39, 31, 23, 15, 7,
	    56, 48, 40, 32, 24, 16, 8,  0,
	    58, 50, 42, 34, 26, 18, 10, 2,
	    60, 52, 44, 36, 28, 20, 12, 4,
	    62, 54, 46, 38, 30, 22, 14, 6
	]

    expansi = [
        31,  0,  1,  2,  3,  4,
	3,  4,  5,  6,  7,  8,
	7,  8,  9, 10, 11, 12,
	11, 12, 13, 14, 15, 16,
	15, 16, 17, 18, 19, 20,
	19, 20, 21, 22, 23, 24,
	23, 24, 25, 26, 27, 28,
	27, 28, 29, 30, 31,  0
        ]
    
    sbox = {
    0: [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
     1: [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
     2: [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
     3: [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]],
     4: [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
     5: [[ 12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]],
     6: [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
     7: [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        }
    
    p_box = [
                15, 6, 19, 20, 28, 11,
		27, 16, 0, 14, 22, 25,
		4, 17, 30, 9, 1, 7,
		23,13, 31, 26, 2, 8,
		18, 12, 29, 5, 21, 10,
		3, 24
        ]

    ip_inv = [39,  7, 47, 15, 55, 23, 63, 31,
		38,  6, 46, 14, 54, 22, 62, 30,
		37,  5, 45, 13, 53, 21, 61, 29,
		36,  4, 44, 12, 52, 20, 60, 28,
		35,  3, 43, 11, 51, 19, 59, 27,
		34,  2, 42, 10, 50, 18, 58, 26,
		33,  1, 41,  9, 49, 17, 57, 25,
		32,  0, 40,  8, 48, 16, 56, 24]

    left_rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    return ip, pc1, pc2, expansi, sbox, p_box, ip_inv, left_rotations

def stringJadiBin(data):
    return ''.join(format(ord(x), 'b').zfill(8) for x in data)

def binJadiString(b=None):
    return ''.join([chr(int(b[x:x+8], 2)) for x in range(0,len(b),8)])

def hexJadiBin():
    "{0:0b}".format(int('5f',16))
    return 0

def IP(i):
    temp_L0_R0 = ''
    for x in range(len(ip)):
        temp_L0_R0 += bin_plaintext[i][ip[x]-1]
    return temp_L0_R0[:len(ip)/2], temp_L0_R0[len(ip)/2:]

def XOR(a, b):
    c = int(a,2)^int(b,2)
    c = "{0:0b}".format(c)
    return c

def PC1():
    temp_E_F = ''
    for x in range(len(pc1)):
        temp_E_F += bin_key[pc1[x]-1]
    return temp_E_F[:len(pc1)/2], temp_E_F[len(pc1)/2:]

def PC2(L, R):
    K0 = L+R
    K = ''
    for x in range(len(pc2)):
        K += K0[pc2[x]-1]
    return K

def EXPANSI(E):
    Exp = ''
    for x in range(len(expansi)):
        Exp += E[expansi[x]-1]
    return Exp

def LEFT_ROT(a, b):
    for x in left_rotations:
        a = a[x:]+a[:x]
        b = b[x:]+b[:x]    
        K.append(PC2(a,b))
    return None

def SBOX(A):
    count = 0
    B = ''
    for x in range(0, len(A), 6):
        a = int(A[x]+A[x+5],2)
        b = int(A[x+1:x+5],2)
        B += "{0:0b}".format(sbox[count][a][b]).zfill(4)
        count += 1

    return B

def P_BOX(B):
    PB = ''
    for x in range(len(p_box)):
        PB += B[p_box[x]-1]
    return PB

def IP_INV(R):
    chiper = ''
    for x in range(len(ip_inv)):
        chiper += R[ip_inv[x]-1]
    return chiper

def DES(itt, itt_plus):
    L0, R0 = IP(i)
    R.append(R0)
    E0, F0 = PC1()
    LEFT_ROT(E0, F0)

    for x in range(16):
        E = EXPANSI(R[x])
        A = XOR(E,K[itt]).zfill(48)
        B = SBOX(A)
        PB = P_BOX(B)
        if x == 0:
            R.append(XOR(L0, PB).zfill(32))
        else:
            R.append(XOR(R[x-1],PB).zfill(32))
        itt += itt_plus
    

def ENCRYPT(bin_iv):
    itt = 0
    itt_plus = 1

    temp = bin_plaintext[i]
    bin_plaintext[i] = bin_iv

    DES(itt, itt_plus)

    temp = XOR(temp, IP_INV(R[16]+R[15])).zfill(64)
    chiper_encrypt.append(temp)
    return IP_INV(R[16]+R[15])

def DECRYPT():
    itt = 0
    itt_plus = 1

    temp = bin_plaintext[i]
    bin_plaintext[i] = bin_iv

    DES(itt, itt_plus)

    temp = XOR(temp, IP_INV(R[16]+R[15])).zfill(64)
    text_decrypt.append(temp)

    return IP_INV(R[16]+R[15]) 
    
def PADDING():
    return 0

if __name__== '__main__':
    ip, pc1, pc2, expansi, sbox, p_box, left_rotations, ip_inv=init()
    mode = 'encrypt'
#    mode = raw_input("encryption

    if mode=='encrypt':
        bin_plaintext=''
        data = raw_input("")

        bin_plaintext = [stringJadiBin(x) for (x) in data]
    elif mode == 'decrypt':
        bin_plaintext=''
        with open('hasil.txt', 'rb') as f:
            data = f.read();

        data = [data[i:i+8] for i in range(0, len(data), 8)]
        bin_plaintext = [stringJadinBin(x) for x in data]
    else:
        print ValueError('Silahkan ketik mode lagi')

    key = 'trykunci'
    IV = '12345678'
    bin_iv = stringJadiBin(IV)
    bin_key = stringJadiBin(key)
    chiper_encrypt = []
    text_decrypt = []

    for i in range(len(bin_plaintext)):
        K = []
        R = []
        if mode == 'encrypt':
            bin_iv = ENCRYPT(bin_iv)
        else:
            bin_iv = DECRYPT()

    if mode == 'encrypt':
        h = ''.join(binJadiString(x) for x in chiper_encrypt)
        print h
