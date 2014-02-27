from Remote import LEDremote
import socket

host = 'localhost'
port = 60000

if __name__ == "__main__":
        #connect to socket
        backlog = 5
        size = 1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen(backlog)
        print("listening for connections on port " , port)

        #initiate remote
        remote = LEDremote()
        while True:
                client, address = s.accept() 
                data = client.recv(size) 
                if data:
                        data = data.split(',')
                        print(data)
                        if (data[0] = "toggle"):
                                remote.toggle(data[1])
                                print('Toggled.\n')
                        elif (data[0] = "level"):
                                remote.levelSet(data[1],data[2])
                                print('Set level.\n')
                        else:
                                print('Invalid command received and ignored.\n')
        client.close()
