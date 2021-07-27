import socket

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8820))
print("please enter your name: ")
name = input()
my_socket.send(name.encode())
data = my_socket.recv(1024).decode()
print("The server sent: " + data)


print("please enter a command: ")
command = input()
length = len(command)
while(command != "time" and command != "rand" and command != "whoru" and command != "exit" and command != "dir"):
    print("please enter a  valid command!! ")
    command = input()
    length = len(command)
while(command != "exit"):
    my_socket.send(command.encode())
    response = my_socket.recv(1024).decode()
    print("The server responded: " + response)
    print("please enter a command: ")
    command = input()
    length = len(command)
"""""
while(command != "exit"):
    if((length < 99) & (length > 10)):
        print(command)
        #command = str(length) + command
        my_socket.send(command.encode())

    elif((length < 10) & (length) > 0):
        print(command + " hihi ")
        #zfill_length = length.zfill(2)
        #command = str(zfill_length) + command
        my_socket.send(command.encode())
        my_socket.recv(1024).decode()
        print("please enter a command: ")
        command = input()
        length = len(command)
"""
my_socket.close()