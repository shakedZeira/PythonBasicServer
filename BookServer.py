import socket
from datetime import datetime
from random import randint
import glob

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 8820))
server_socket.listen()
print("the server is running")

(client_socket , client_address) = server_socket.accept()
print("client connected")

data = client_socket.recv(1024).decode()
print("client sent: " + data)

reply = "Hello " + data
client_socket.send(reply.encode())

#length = client_socket.recv(2).decode()
#command = client_socket.recv(int(length)).decode()

command = client_socket.recv(1024).decode()
print("client command: " + command)

while(command != "exit"):
    if(command == "time"):
        time_now = str(datetime.now().time())
        print(time_now)
        client_socket.send(time_now.encode())
    elif(command == "rand"):
        random_number = str(randint(1,10))
        print(random_number)
        client_socket.send(random_number.encode())
    elif(command == "whoru"):
        server_name = "marco"
        print(server_name)
        client_socket.send(server_name.encode())
    elif(command == "exit"):
        client_socket.close()
        server_socket.close()
        break
    elif(command =="dir"):
        files_list = str(glob.glob(r'C:\C:\Users\shake\PycharmProjects\*.*'))
        for i in range(len(files_list)):
            print(files_list[i] + "lol")
        client_socket.send(files_list.encode())

    command = client_socket.recv(1024).decode()
    print("client command: " + command)

client_socket.close()
server_socket.close()