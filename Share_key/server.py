# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:08:29 2017

@author: MHR7
"""

#python version: Python 3.5 for Windows
import socket
import sys
from thread import *

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "starting server"

#menerima koneksi dari semua interface
server_address=('localhost',10010)
client_list=list()

def send_to_all_klien(message):
    for koneksi in client_list:
        try:
            koneksi.sendall(message)
        except:
            koneksi.close()
            client_list.remove(koneksi)
            
def klien(koneksi):
    while True:
        try:
            data = koneksi.recv(1024)
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