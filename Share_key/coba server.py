#python version: Python 3.5 for Windows
import socket
import sys
from thread import *
from random import getrandbits
import math

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "starting server"

#menerima koneksi dari semua interface
server_address=('localhost',10300)
client_list=list()

# Input

if __name__ == "__main__":
    print("n = ")
    n = input("")
    print("g = ")
    g = input("")
    bits = 32
    print("input selesai")    
   
# Alice (x, X)
    x = getrandbits(bits)
    X = pow(g, x, n)

# Bob (y, Y)
    y = getrandbits(bits)
    Y = pow(g, y, n)

# Perbandingan hasil
    A = pow(Y, x, n)
    B = pow(X, y, n)
    A2= str(A)

    if(A == B):
        print("Angka rahasia cocok: ", A2)
 


def send_to_all_klien(A2):
    for koneksi in client_list:
        try:
            koneksi.sendall(A2)
        except:
            koneksi.close()
            client_list.remove(koneksi)
            
def klien(koneksi):
    while True:
        try:
            data = koneksi.recv(1024)
            
            KUNCIB = (int(data), x, n)
            kunciB = str(KUNCIB)
            i = len(kunciB)
            j = 0
            if len(kunciB) < 8 :
                for i in range(len(kunciB), 8):
                    i+=1
                    j+=1
                    kunciB = kunciB + str(j)
            print kunciB
            print >>sys.stderr, 'connection from', client_address
            data = connection.recv(40)
                       
            
            if data:
                send_to_all_klien(data)
            else:
                break
        except:
            koneksi.close()
            break
            
sock.bind(server_address)
sock.listen(1)

"starting to listen"
while True:
    koneksi,addr=sock.accept()
    client_list.append(koneksi)
    start_new_thread(klien,(koneksi,))

koneksi.close()
sock.close()
