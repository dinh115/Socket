import socket
from web import *


        

class GetRequest:
    def __init__(self,conn):
        request = ""
        conn.settimeout(3)
        try:
            request = conn.recv(1024).decode()
            while(request):
                request += conn.recv(1024).decode()
        except socket.timeout:
            print("No request!!!")
        finally:
            if (request != ""):
                login = request.split("\n")[-1]
                request = request.split("\n")[0]
                self.type = request.split(" ")[0]
                self.path = request.split(" ")[1]
                if (self.type == "POST"):
                    print(login)
                    self.username =  (login.split("=")[1]).split("&")[0]
                    self.password = (login.split("=")[2]).split("&")[0]
            else:
                self.type = None

def login():
    # in case We have many admin account
    f = open("web/name.txt","r").read().split('\n')
    

    

def new_account(uname,psw):
    f = open("web/name.txt","a")
    f.write(uname,"-",psw,"\n")
    f.close()

def GetResponse(request,conn):
    conn.sendall(rsp(request.path,request).Load())

def PostResponse(request,conn):
    if (request.username == "admin" and request.password == "123456"):
        conn.sendall(rsp(request.path,request).Load())
    else:
        conn.sendall(rsp("/401.html").Load())


    


    
login()

        
        

        



