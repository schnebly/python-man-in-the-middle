import socket, threading

class Client(threading.Thread):
    def run(self):
        spacing = ""
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(spacing, "open")

        requestData = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]

        for datum in requestData:
            print(spacing, "put:", datum)
            connection.sendto(datum.encode("utf8"), clientAddress)

            responseData, clientAddress = connection.recvfrom(1024)
            print(spacing, "get:", responseData.decode("utf8"))

        connection.close()
        print(spacing, "close")

class Server(threading.Thread):
    def run(self):
        count = 0
        spacing = "\t\t\t"
        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connection.bind(serverAddress)

        print(spacing, "open")

        while 1:
            requestData, clientAddress = connection.recvfrom(1024)
            print(spacing, "get:", requestData.decode("utf8"))

            count += 1

            if requestData.decode("utf8") == ".":
                responseData = "done"
            else:
                responseData = "ok [" + str(count) + "]"

            print(spacing, "put:", responseData)
            connection.sendto(responseData.encode("utf8"), clientAddress)

            if requestData.decode("utf8") == ".":
                break

        connection.close()
        print(spacing, "close")

class Attacker(threading.Thread):
    def run(self):
        spacing = "            "
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        clientConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientConnection.bind(clientAddress)

        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        serverConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(spacing, "open")

        while 1:
            clientRequestData, clientAddress = clientConnection.recvfrom(1024)
            print(spacing, "get:", clientRequestData.decode("utf8"))

            serverRequestData = clientRequestData.decode("utf8")

            print(spacing, "put:", serverRequestData)
            serverConnection.sendto(serverRequestData.encode("utf8"), serverAddress)

            serverResponseData, serverAddress = serverConnection.recvfrom(1024)
            print(spacing, "get:", serverResponseData.decode("utf8"))

            clientResponseData = serverResponseData.decode("utf8")

            print(spacing, "put:", clientResponseData)
            clientConnection.sendto(clientResponseData.encode("utf8"), clientAddress)

            if serverResponseData.decode("utf8") == "done":
                break

        serverConnection.close()
        clientConnection.close()
        print(spacing, "close")

print("  Client     Attacker     Server")
print("----------  ----------  ----------")

server = Server()
attacker = Attacker()
client = Client()

server.start()
attacker.start()
client.start()

server.join()
attacker.join()
client.join()