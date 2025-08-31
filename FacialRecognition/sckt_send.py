import os 
from socket import * 

def send_until_recv(data):
    host = "192.168.15.242" # set to IP address of target computer 
    port = 13000 
    buf = 1024 
    addr = (host, port) 
 
    UDPSock = socket(AF_INET, SOCK_DGRAM) 

    while True: 
        UDPSock.sendto(data.encode(), addr) 
        
        (data, addr) = UDPSock.recvfrom(buf) 
        if data.decode() == "400": 
            break 
        
    UDPSock.close()
