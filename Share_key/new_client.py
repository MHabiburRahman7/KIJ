import socket
import sys
import DES_encrypt
import DES_decrypt

prima = 23
basis = 5

a = input("Random key : ")
A = pow(basis, a, prima)
print "isi A: ",A
A = str(A)

host = 'localhost'
port = 10100
size = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (host, port)
print ('connecting to %s port %s ' % server_address)
sock.connect(server_address)

sock.send(A)

try:
    while True:
        # Send data
        pesan = input('Kirimkan pesan : ')
        sock.sendall(pesan.encode('utf-8'))
        # Look for the response
        data = sock.recv(32)
        if data:
            print ('received from server "%s" ' % data)
        else:
            break
finally:
    print ('closing socket')
    sock.close()
