# -*- coding: utf-8 -*-
"""
Created on Wed May 10 03:49:19 2017

@author: MHR7
"""

""" 
An echo server that uses threads to handle multiple clients at a time. 
Entering any line of input at the terminal will exit the server. 
""" 

import socket 
import sys 
import threading 
import pickle
import new_rsa

class Server:         
    def __init__(self): 
        self.host = ''
        self.port = 10040
        self.backlog = 5 
        self.size = 1024 
        self.server = None 
        self.threads = []

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
    
    public_mereka = []

    def __init__(self,(client,address)): 
        threading.Thread.__init__(self) 
        self.client = client 
        self.address = address 
        self.size = 1024
        
        self.kunci_publik, self.kunci_privat = new_rsa.get_keys()
        
        self.client.send(pickle.dumps(self.kunci_publik))
        print "Kunci publik yang di dikirim:", self.kunci_publik
        
        
    def run(self):
        incoming = self.client.recv(self.size)
        incoming_arr = pickle.loads(incoming)
        public_mereka = incoming_arr
        
        print "Kunci publik yang di terima:", public_mereka
        
        running = 1 
        
        while running:
             incoming = self.client.recv(self.size)
             incoming_arr = pickle.loads(incoming)
             real_data = new_rsa.decrypt(incoming_arr, self.kunci_privat)
             print "client %s : %s" %(self.address, real_data.strip())
                
             data = raw_input()
             data = new_rsa.encrypt(data, public_mereka)
             print 'Decrypt : ', data
             self.client.send(pickle.dumps(data))

if __name__ == "__main__": 
    s = Server()
    print 'waiting client ....\n\n'
    #counter=0
    s.run()