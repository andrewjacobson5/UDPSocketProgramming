import random
import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('localhost', 8080))

serverName = "Server of Andrew"
while True:
    random_int = random.randint(1, 100)
    print("ready to receive message")
    data, addr = socket.recvfrom(1024)
    if data.decode() == "exit":
        break
    decoded_dataName = data.decode()
    
    # Wait for int input
    data, addr = socket.recvfrom(1024)
    decoded_dataNumber = data.decode()
    if int(decoded_dataNumber) < 1 or int(decoded_dataNumber) > 100:
        break
    
    print(data.decode("utf-8"), "is from ", decoded_dataName, "@", addr)
    
    socket.sendto(serverName.encode("utf-8"), addr)
    
    msg_number = str(random_int)
    socket.sendto(msg_number.encode("utf-8"), addr)

    msg_clientNumber = decoded_dataName + "'s number is " + decoded_dataNumber
    socket.sendto(msg_clientNumber.encode("utf-8"), addr)

    #msg = "Message from: " + serverName + "\n" + decoded_dataName + "'s number is " + data.decode("utf-8") + " my number is " + str(random_int)
    #socket.sendto(msg.encode(), addr)
    