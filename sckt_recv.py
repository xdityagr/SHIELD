import os 
from socket import * 


def recv_data():
    host = "" 
    port = 13000 
    buf = 1024 
    addr = (host, port) 
    UDPSock = socket(AF_INET, SOCK_DGRAM) 
    UDPSock.bind(addr) 
    
    recieved = None
    print("Waiting to receive messages...") 
    while True: 
        (data, addr) = UDPSock.recvfrom(buf) 
        recieved = data.decode()
        
        UDPSock.sendto('400'.encode(), addr) 
        break
        
    UDPSock.close()
    return recieved 
