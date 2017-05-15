import random
import math
import numpy as np

#n_e_d = []

def primesfrom3to():
    n=5000
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

def prime_new(interval):
    prime_list = []

    for i in range(2, interval + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    
    ada = len(prime_list)
    p_num =np.random.randint(0, ada)
    q_num =np.random.randint(0, ada)
    while(p_num == q_num):
        q_num =np.random.randint(0, ada)
    
    return prime_list[p_num], prime_list[q_num]

def primeNr(interval):
    prime_list = []
    
    for i in range(2, interval + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    
    return prime_list
"""
def generate_p(batas_max):

    # initialising primes
    minPrime = 0
    maxPrime = batas_max
    cached_primes = [i for i in range(minPrime,maxPrime) if isPrime(i)]

    n = random.choice([i for i in cached_primes if p<i<q])
    
    return n;
"""

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
    
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def hitung_d(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
"""

def hitung_d(m, e):
    d = 0
    # Mencari kunci privat (d) 
    for j in range(3, m, 2):
        print "Nilai j",j
        if j * e % m == 1:
            d = j
            break
    print "Nilai d: ",d
    return d
"""
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
        temp = pow(int(l[i]), int(e), int(n))
#        int_pow = int(l[i])** int(e)
#        mod_pow = int_pow % int(n)
        enkrip.append(int(temp))  
        #print enkrip[i]
        i+=1
    
    #enkripsi = ','.join(map(str,enkrip))
    #enk = list(enkripsi)
    #print enkripsi
    #print "Hasil enkripsi: "+enkripsi
    return enkrip
    
def decrypt(code, private_key):
    
    d, n = private_key
    d = int(d)
    n = int(n)
    code = list(code)
#    print type(code)
#    code = code1
#    d = n_e_d[2]
#    n = n_e_d[0]

    dekrip = []
    i=0

    while i<len(code):
        int_code = int(code[i])
        print "asli: ", int_code
        temp = pow(int_code, d, n)
#        int_pow = int(code[i])** int(d)
#        mod_pow = int_pow % int(n)
        dekrip.append(int(temp))
        print dekrip[i]
        i+=1
        

    #print "selesai while"
    dekripsi = ''.join(chr(i) for i in dekrip)
    #print "Hasil dekripsi: ",dekrip
    return dekripsi
        
def get_all():
    p, q = primesfrom3to()
    n = hitung_n(p,q)
    m = hitung_m(p,q)
    e = hitung_e(n)
    d = hitung_d(m,e)
    
    return p, q, n, m, e, d
    

def init_rsa():
#    k = 0
#    n_e_d = []
    batas_max = 300
   # prim = []
#    enkrip = []
#    dekrip = []
#    p = rand_p(batas_max)
#    q = rand_q(batas_max)

    p, q = primesfrom3to()

    print p," dan ",q
    
    n = hitung_n(p, q)
#    n_e_d.append(n)
    m = hitung_m(p, q)
    
    e = hitung_e(m)
#    n_e_d.append(e)
    d = hitung_d(m, e)
#    n_e_d.append(d)
    
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
    
if __name__ == "__main__":
    batasan = 1000
    
    #p, q = primesfrom3to()
    p, q = prime_new(batasan)
    #n = hitung_n(p,q)
    n = p * q
    #m = hitung_m(p,q)
    m = (p-1)*(q-1)
    e = hitung_e(n)
    d = hitung_d(m,e)
      
    public_key = []
    private_key = []
    public_key.append(e)
    public_key.append(n)
    private_key.append(d)
    private_key.append(n)
    print "public key: ", public_key
    print "private key: ", private_key
    
    plaintext = raw_input('plaintext : ')
    
    enkr = encrypt(plaintext, public_key)
    dekr = decrypt(enkr, private_key)
    
    #print "Hasil enkripsi: ",enkr
    print "Hasil dekripsi: ",dekr
    