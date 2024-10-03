import socket 
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 8080

msg_name = input("Input your name: ")

if msg_name == "exit":
    exit("Exiting")
socket.sendto(msg_name.encode("utf-8"), (host, port))
msg_number = input("Input an integer between 1 and 100: ")

if int(msg_number) < 1 or int(msg_number) > 100:
    exit("Invalid input")

msg_number = msg_number.encode("utf-8")

socket.sendto(msg_number, (host, port))
if msg_number.decode() == "exit":
    exit("Exiting")

server_msgName = socket.recvfrom(1024)
decoded_server_msgName = server_msgName[0].decode()
print("Received Message from: " + decoded_server_msgName)

server_msgNum = socket.recvfrom(1024)
print(decoded_server_msgName +"'s number is: " + server_msgNum[0].decode("utf-8"))

server_msg = socket.recvfrom(1024)
print(server_msg[0].decode("utf-8"))

print("The sum of the two numbers is: " + str(int(msg_number.decode()) + int(server_msgNum[0].decode("utf-8"))))