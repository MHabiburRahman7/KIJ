# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:10:58 2017

@author: MHR7
"""

import numpy as np

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modular_inv(e, m):
    g, x, y = egcd(e, m)
    if g != 1:
        raise Exception('modular inverse tidak tersedia')
    else:
        return x % m
        

def fpb(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primes_p_and_q():
        """ Returns a array of primes, p < n """
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
        
def get_keys():
    #dapatkan nilai p dan q
    p, q = primes_p_and_q()
    #hitung nilai n
    n = p * q
    #hitung nilai m
    m = (p-1)*(q-1)
    #e sifatnya bebas, jadi dirandom saja
    e = np.random.randint(1, m)
    
    temp = fpb(e, m)
    
    #fpb harus ==1 untuk modular invers
    while temp != 1:
        e = np.random.randint(1, m)
        temp = fpb(e, m)
        
    d = modular_inv(e,m);
    return ((long(e), long(n)), (long(d), long(n)))

def encrypt(plaintext, public_key):
    
    e, n = public_key
    enkrip = []
    for i in plaintext:
        temp = pow(ord(i), e, n)
        enkrip.append(temp)
    return enkrip

def decrypt(code, privat_key):
    
    d, n = privat_key
    dekrip = []
    for i in code:
        temp = chr(pow(i, d, n))
        dekrip.append(temp)
    return ''.join(dekrip)

    