import socket 
import time

host = 'localhost' 
port = 60000
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
while True:
        s.send('toggle,blue,2')
        time.sleep(1)
        s.send('toggle,red,2')
        time.sleep(1)
        s.send('toggle,green,2')
        time.sleep(1)
        s.send('toggle,red,2')
        time.sleep(1)
        s.send('toggle,blue,2')
        time.sleep(1)
        s.send('toggle,green,2')
        time.sleep(1)
        print 'Sent'
