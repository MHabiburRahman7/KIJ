# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:36:03 2017

@author: MHR7
"""
import sys
import socket
import DES_encrypt
import DES_decrypt

host = 'localhost'
port = 10100
size = 1024
server_address = (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

prima = 23
basis = 5

a = input("Random key : ")
a = int(a)
A = pow(basis, a, prima)
print "isi A: ", A
A = str(A)

s.bind(server_address)
#sock.settimeout(15)
print (s.gettimeout())

# Listen for incoming connections
s.listen(5)

while True:
    # Wait for a connection
    print ('waiting for a connection ');
    connection,client_address = s.accept()
    #print ('connected from %s', client_address);
    
    
    try:
        print ('connection from', client_address);
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print ('received from flient : "%s"' % data.decode());
            if data:
                pesan=input('Kirim pesan: ')
                connection.sendall(pesan.encode('utf-8'))
            else:
                print ('no more data from', client_address);
                break
    finally:
        # Clean up the connection
        connection.close()
#        sock.close()
