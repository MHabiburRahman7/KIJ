import random
import numpy as np

#n_e_d = []

def primesfrom3to():
    n=700
    assert n>=2
    sieve = np.ones(n/2, dtype=np.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    z= np.r_[2, 2*np.nonzero(sieve)[0][1::]+1] 
    temp = np.random.randint(95,len(z))
    temp2 = np.random.randint(95,len(z))
    if temp2 == temp:
        temp2 = np.random.randint(95,len(z))
    return z[temp], z[temp2]


def rand_p(batas_max):
    """    
    bedebah = int(raw_input()) 	# Range nilai untuk menentukan random nilai p dan q
    """
    prima = True
    while (prima) :	# Menentukan nilai prima p dan nilai p dirahasiakan
        p = random.randint(2,batas_max)
        prima = True
        for j in range (2,p) :
            if p%j==0 & j != p: 
                prima = False
        if(prima == True):
            print "nialai p: ",p
            break
    return p

def rand_q(batas_max):
    prima = True
    while (prima) :	# menentukan nilai prima q dan nilai q dirahasiakan
        q = random.randint(2,batas_max)
        for j in range (2,q) :
            if(q%j==0) & q != j: 
                prima = False
        if(prima == True):
            print "Nilai q: ",q
            break
    return q

def hitung_n(p, q):
    n = p*q # nilai n tidak dirahasiakan
    #print "Niali n: ",n
    return n

def hitung_m(p, q):
    m = (p-1)*(q-1) # nilai m perlu dirahasiakan
    #print "Niali m: ",m
    return m
    
# Mencari faktor terbesar
def gcd(a, b):
	for n in range(2, min(a, b) + 1):
		if a % n == b % n == 0:
			return False
	return True
 
def hitung_e(m):
    # Memilih kunci publik (e) yang relatif prima terhadap m
    for i in range(3, m, 2):
        i = random.randint(3,m)
        if gcd(i, m) == 1:
            e = i
            break
    #print "Nilai e: ",e
    return e

def hitung_d(m, e):
    d = 0
    # Mencari kunci privat (d) 
    for j in range(3, m, 2):
        if j * e % m == 1:
            d = j
            break
    #print "Nilai d: ",e
    return d

def cek_kunci(e, d, n):
    #print "Nilai d: ",d
    kunci_public = [e,n]
    print "Kunci Publik: ",kunci_public
    kunci_privat = [d,n] 
    print "Kunci Private: ",kunci_privat
    
    
#-----------------------saving txt----------------------------
def saving_key(e, d, n):
    with open('kuncipublik.txt', 'wb') as file:
        file.write("%d, %d" % (e, n))

    with open('kunciprivat.txt', 'wb') as file:
        file.write("%d, %d" % (d, n))
#------------------------enkripsi-----------------------------

"""
print l
i = 0
while i < len(plaintext):
    enkrip.append((l[i] ** e) % n)  
    #print enkrip[i]
    dekrip.append((enkrip[i] ** d) % n)
    i+=1
    
enkripsi = ''.join(map(str,enkrip))
print "Hasil enkripsi: "+enkripsi
dekripsi = ''.join(chr(i) for i in dekrip)
print "Hasil dekripsi: "+dekripsi

"""

def encrypt(plaintext, public_key):    
    e, n = public_key
    enkrip = []
    i=0
    text = list(plaintext)
    #print text
    l = [ord(c) for c in text]
    while i<len(plaintext):
        #l[i] = int(l[i])
        int_pow = int(l[i])** int(e)
        mod_pow = int_pow % int(n)
        enkrip.append(int(mod_pow))  
        #print enkrip[i]
        i+=1
    
    enkripsi = ','.join(map(str,enkrip))
    #enk = list(enkripsi)
    #print enkripsi
    #print "Hasil enkripsi: "+enkripsi
    return enkrip
    
def decrypt(code, private_key):
    
    #code = int(code)
    d, n = private_key
#    d = n_e_d[2]
#    n = n_e_d[0]
    dekrip = []
    i=0
    #tampung = code.split(",")
    #print tampung
    """
    while i<len(code):
        if(code[i]!=' '):
            tampung.append(code[i])
        
        else:
            continue
        
        i+=1
    i=0
    """
    while i<len(code):
        int_pow = int(code[i])** int(d)
        mod_pow = int_pow % int(n)
        dekrip.append(int(mod_pow))
        #print dekrip[i]
        i+=1
        

    #print "selesai while"
    dekripsi = ''.join(chr(i) for i in dekrip)
    #print "Hasil dekripsi: "+dekripsi
    return dekripsi
        
#if __name__ == "__main__":
def init_rsa():
#    k = 0
    n_e_d = []
    batas_max = 60
   # prim = []
#    enkrip = []
#    dekrip = []
#    p = rand_p(batas_max)
#    q = rand_q(batas_max)

    p, q = primesfrom3to()

    print p," dan ",q
    
    n = hitung_n(p, q)
    n_e_d.append(n)
    m = hitung_m(p, q)
    
    e = hitung_e(m)
    n_e_d.append(e)
    d = hitung_d(m, e)
    n_e_d.append(d)
    
    saving_key(e, d, n)
    cek_kunci(e, d, n)
    
    """
    print "n_e_d: "
    #x = 0
    for x in range(0, len(n_e_d)):
        print n_e_d[x]
    """
    
    return n_e_d
"""    
def get_n():
    return n_e_d[0]

def get_e():
    return n_e_d[1]

def get_d():
    return n_e_d[2]
    
"""
    #self.cek_kunci(e,d,n)
"""
    plaintext = raw_input('plaintext : ')
    text = list(plaintext)
    l = [ord(c) for c in text]

"""
    
	




















