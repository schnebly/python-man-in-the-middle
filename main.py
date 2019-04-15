import socket, threading

class Client(threading.Thread):
    def run(self):
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class Server(threading.Thread):
    def run(self):
        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connection.bind(serverAddress)

class Attacker(threading.Thread):
    def run(self):
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        clientConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientConnection.bind(clientAddress)

        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)
        
        serverConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)