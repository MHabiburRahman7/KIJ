# -*- coding: utf-8 -*-
"""
Created on Tue May 09 20:52:56 2017

@author: MHR7
"""

#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

import socket
import sys
import pickle
import new_rsa

kunci_publik, kunci_privat = new_rsa.get_keys()

host = 'localhost'
port = 10040
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

print "connect to port: "+host,port

#Pengiriman kunci publik

incoming = pickle.loads(s.recv(size))
public_mereka = incoming
print "Kunci publik yang di terima:", public_mereka
        
public_kita = pickle.dumps(kunci_publik)
s.sendall(public_kita)
print "Kunci publik yang di kirim:", kunci_publik 

print "Mulai chat server"

while 1:
    get_public = True
    
    data = sys.stdin.readline()
    data = raw_input()
            
    data_send = pickle.dumps(new_rsa.encrypt(data, public_mereka))
    s.sendall(data_send)
    
    data = pickle.loads(s.recv(size))
        
    real_data = new_rsa.decrypt(data, kunci_privat)
    print 'server : ' + real_data.strip()
    
s.close()
