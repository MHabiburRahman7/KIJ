# -*- coding: utf-8 -*-
"""
Created on Wed May 10 03:49:19 2017

@author: MHR7
"""

""" 
An echo server that uses threads to handle multiple clients at a time. 
Entering any line of input at the terminal will exit the server. 
""" 

import select 
import socket 
import sys 
import threading 
import pickle
import rsa_plain

class Server:         
    def __init__(self): 
        self.host = ''
        self.port = 10210
        self.backlog = 5 
        self.size = 1024 
        self.server = None 
        self.threads = []
        rsa_plain.init_rsa()

    def open_socket(self): 
        try: 
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            self.server.bind((self.host,self.port)) 
            self.server.listen(5) 
        except socket.error, (value,message): 
            if self.server: 
                self.server.close() 
            print "Could not open socket: " + message 
            sys.exit(1) 

    def run(self): 
        self.open_socket() 
        input = [self.server]
        running = 1 
        
        while running: 
            c = Client(self.server.accept()) 
            c.start() 
            self.threads.append(c)

        # close all threads 

        self.server.close() 
        for c in self.threads: 
            c.join() 

class Client(threading.Thread):

    def __init__(self,(client,address)): 
        threading.Thread.__init__(self) 
        self.client = client 
        self.address = address 
        self.size = 1024
        
        file1 = open("kuncipublik.txt", "r")
        file2 = open("kunciprivat.txt", "r")
    
        temp = file1.read()
        self.public_key = temp.split(",")
    
        temp = file2.read()
        self.private_key = temp.split(",")
        
#        self.public_key, self.private_key = public_key, private_key
#        self.public_key_partner = pickle.loads(self.client.recv(self.size))
#        self.client.send(pickle.dumps(self.public_key))
        
    def run(self): 
        running = 1 
        
        while running:
            
            incoming = self.client.recv(self.size)
            incoming_arr = pickle.loads(incoming)
            real_data = rsa_plain.decrypt(incoming_arr, self.private_key)
            print "client %s : %s" %(self.address, real_data.strip())
            
            data = raw_input()
            print 'Decrypt : '+ data
            data = rsa_plain.encrypt(data, self.public_key)
            self.client.send(pickle.dumps(data))
"""
#            sign_data = pickle.loads(self.client.recv(self.size))
            
#            if sign_data: 

#                real_data =''
#                real_data += data

#                while real_data[len(real_data)-3:len(real_data)]!='~~~':
#                    data = self.client.recv(self.size)
#                    real_data += data
#                data = pickle.loads(self.client.recv(self.size))    
#                print sign_data
#                sign_data_in = verifikasi(self.public_key, self.public_key_partner, sign_data)
                print sign_data_in
                
                if sign_data_in == 'verifikasi gagal':
                    continue
                
                real_data = decrypt(self.private_key,data)
                print "client %s : %s" %(self.address, real_data.strip())
                
#                print 'key : '+self.key
                print '>> %s : ' %(self.address, ),
                data = raw_input()
                   
                
                data = encrypt(self.public_key_partner,data)
#                print 'Decrypt : '+ data
"""                
            
#                self.client.send('~~~')

            #else: 
            #    self.client.close() 
            #    running = 0 

if __name__ == "__main__": 
    s = Server()
    print 'waiting client ....\n\n'
    #counter=0
    s.run()