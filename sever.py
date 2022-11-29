import socket
import threading
from request import *

#define
HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("Server ready")
print("listening in port 8080:")

def handleClient(conn,addr):
    while True:
        request = GetRequest(conn)
        if (request.type != None):
            if (request.type == "GET"):
                GetResponse(request,conn)
            if (request.type == "POST"):
                PostResponse(request,conn)


while True:
    try:
        conn,addr = server.accept()
        print(addr,"connected")
        ThreadClient = threading.Thread(target=handleClient,args=(conn,addr))
        ThreadClient.daemon = True 
        ThreadClient.start()
    except:
        conn,addr = server.accept()
        conn.sendall(rsp("/404.html"))


server.close()
print("END")
