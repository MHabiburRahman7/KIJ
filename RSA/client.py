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
import rsa_plain

file1 = open("kuncipublik.txt", "r")
file2 = open("kunciprivat.txt", "r")

host = 'localhost'
port = 10210
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

print "connect to port: "+host,port

temp = file1.read()
public_key = temp.split(",")

temp = file2.read()
private_key = temp.split(",")
 
#public_key, private_key = 
#s.send(pickle.dumps(public_key))
#public_key_partner = pickle.loads(s.recv(size))

while 1:
    # read from keyboard
    print '>> ',
    data = sys.stdin.readline()
    data = raw_input()

    if data== '\n':
        break
    
    #sign_data = sign(private_key, public_key_partner)
    data_send = pickle.dumps(rsa_plain.encrypt(data, public_key))
    s.sendall(data_send)
#    print 'Decrypt : '+ str(data)
#    print 'public key : '+str(public_key_partner)
#    s.send(pickle.dumps(sign_data))
#    s.send(pickle.dumps(data))
#    s.send('~~~')

    data = pickle.loads(s.recv(size))
    
    real_data = rsa_plain.decrypt(data, private_key)
    print 'server : ' + real_data.strip()
    
s.close()
