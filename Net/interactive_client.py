#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

import sys
import socket

class Client():
    def __init__(self, addr, mode):
        self.host = addr[0]
        self.port = addr[1]
        self.mode = mode
        self.sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def run(self):
        if self.mode == 'interactive':
            self.interactive()
        else:
            print('{} is not implemented'.format(self.mode))
            
    def interactive(self):
        self.sockobj.connect((serverHost, serverPort))
        
        while True:
            self.sockobj.settimeout(1) # таймаут для чтения всех данных
            data = self.sockobj.recv(1024).decode()
            print(data)
            
            if data == 'Timeout' or data == 'Wrong':
                break
            
            line = input('> ')
            self.sockobj.send(line.encode())
        
        self.sockobj.close()
    
    def read_data(self):
        data = self.sockobj.recv(1024)
        # чтение всех данных
        buffer = b''
        while data:
            buffer += data
            try:
                data = self.sockobj.recv(1024)
            except socket.error:
                break
        return buffer.decode()
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: interactive_client <host> <port> <mode>')
        exit(0)
    
    serverHost = sys.argv[1]
    serverPort = int(sys.argv[2])
    mode = sys.argv[3]

    clientobj = Client((serverHost, serverPort), mode)
    clientobj.run()
    