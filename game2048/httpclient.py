from src.controller import controller
import socket
import sys

HOST = 9999
PORT = "localhost"

game = controller(4)

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

data = game.getBoard()

sock.sendall(bytes(str(data)), "utf-8")

received = str(sock.recv(1024), "utf-8")
print(received)
