import os

# Use absolute path instead of realtive
# The installer should change it to the path to the this file
os.chdir('C:/Users/ADMIN/Documents/Computer Network/SOCKET/python2')

def getFullpath(page):
    Files = list()
    Page = os.listdir(page)
    for i in Page:
        fullpath = page +  "/" + i
        if os.path.isdir(fullpath):
            Files = Files + getFullpath(fullpath)
        else:
            Files.append(fullpath)

    return Files

def TypeofFiles(type):
    switcher = {
        "txt" : "test/plain",
        "jpg" : "image/jpeg",
        "jpeg": "image/jpeg",
        "gif" : "image/gif",
        "png" : "image/png",
        "css" : "text/css",
    }
    #in case application/octet-stream, we load file 404.html
    return switcher.get(type,"text/html")


class rsp:
    def __init__(self,path,request):
        if path == "/":
            path = "/index.html"

        self.ContentType = TypeofFiles(path.split(".")[-1])
        
        self.path = "web" + path
        AllFiles = getFullpath("web")
        if (self.path in AllFiles):
            if (path == "web/images.html"):
                f = open("web/name.txt","r")
                type = f.read().split('\n')[0]
                if (type == "GET"):
                    self.path = "/401.html"
                    midheader = "401 Unauthorized"
            elif (path == "/401.html"):
                midheader = "401 Unauthorized"
            elif (path == "/404.html"):
                midheader = "404 Not Found"
            else:
                midheader = "200OK"
        else:
            midheader = "404 Not Found"
            self.path = "web/404.html"

        self.header = "HTTP/1.1 " + midheader +"\r\n" + self.ContentType+"\r\n"
    
    def Load(self):
        self.data = open(self.path,"rb").read()
        return (self.header + "Content-Length:"+ str(len(self.data)) +"\r\n\r\n").encode("utf-8") + self.data + "\r\n".encode("utf-8")


