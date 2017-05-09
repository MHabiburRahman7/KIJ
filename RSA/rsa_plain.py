import random
import math

bedebah = int(raw_input()) 	# Range nilai untuk menentukan random nilai p dan q
k = 0
prim = []
for i in range (2,bedebah) :	# Menentukan nilai prima p dan nilai p dirahasiakan
	p = random.randomint(2,bedebah)
	prima = True
	for j in range (2,p) :
		if(p%j==0) : prima = False

	if(prima== True):
		print p
		break
for i in range (2,bedebah) :	# menentukan nilai prima q dan nilai q dirahasiakan
	q = random.randomint(2,bedebah)
	prima = True
	for j in range (2,q) :
		if(q%j==0) : prima = False

	if(prima == True):
		print q
		break
n = p*q # nilai n tidak dirahasiakan
print  n

m = (p-1)*(q-1) # nilai m perlu dirahasiakan
print m

# Mencari faktor terbesar
def gcd(a, b):
	for n in range(2, min(a, b) + 1):
		if a % n == b % n == 0:
			return False
	return True


# Memilih kunci publik (e) yang relatif prima terhadap m
for i in range(3, m, 2):
	i = random.randomint(3,m)
	if gcd(i, m) == 1:
		e = i
		break
print e

# Mencari kunci privat (d) 
for j in range(3, m, 2):
	if j * e % m == 1:
		d = j
		break

print d


kunci_public = [e,n]
print kunci_public
kunci_privat = [d,n] 
print kunci_privat
#-----------------------saving txt----------------------------
with open('kuncipublik.txt', 'wb') as file:
	file.write("%d %d" % (e, n))

with open('kunciprivat.txt', 'wb') as file:
	file.write("%d %d" % (d, n))
#------------------------enkripsi-----------------------------
# plaintext = raw_input('plaintext : ')
# s = list(plaintext)
# l = [ord(c) for c in s]
# enkrip = []
# dekrip = []
# print l
# i = 0
# while i < len(plaintext):
# 	enkrip.append((l[i] ** e) % n)  
# 	print enkrip[i]
# 	dekrip.append((enkrip[i] ** d) % n) 
# 	print dekrip[i]
# 	i+=1

# enkripsi = ''.join(map(str,enkrip))
# print enkripsi
# dekripsi = ''.join(chr(i) for i in dekrip)
# print dekripsi

	




















