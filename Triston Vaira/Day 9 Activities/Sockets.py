import socket
import os

def udp_echo_service():
    while True:
        s = socket.socket(type=socket.SOCK_DGRAM)
        s.bind(('', 12345))
        print("Attempting to receive...")
        dgram, address = s.recvfrom(4096) #blocks
        print(dgram, 'Received from ', address)
        s.sendto(dgram, address)
 
##############################################################################
##############################################################################

def udp_echo_client():
    s = socket.socket(type=socket.SOCK_DGRAM)
    dgram = b'import os; os.getcwd'
    s.sendto(dgram,('192.168.250.150', 12345))
    print(dgram, ' sent')
    echodata, address = s.recvfrom(4096)
    print (echodata, ' echoed back from ', address)
    
##############################################################################
##############################################################################
    
def tcp_qotd_service():
    s = socket.socket()
    server_s.bind(('',12345))
    server_s.listen()
    
    client_s, address = server_s.accept() # blocks
    quote = b'i will delete this file'
    client_s.send(quote)
    
    client_s.close()
    server_s.close()

##############################################################################
##############################################################################

def tcp_qotd_client():
    s = socket.socket()
    s.connect(('10.50.33.65', 12346)) # blocks
    s.sendall(b'never gonna give you up')
    data = s.recv(16)
    quote = bytearray()
    while data:
        print(quote)
        quote.extend(data)
        data = s.recv(16)
    print(quote.decode('ascii'))

##############################################################################
##############################################################################
    
if __name__ == '__main__':
 tcp_qotd_client()
 
