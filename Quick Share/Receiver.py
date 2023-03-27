import json
import socket, os , threading
Receiver = socket.socket()
Ip,Port = "127.0.0.1",9090 #Change to your local Ip
Receiver.bind((Ip,Port))
Receiver.listen(2)
Directory = "PyReceiver"
def Main():
    while 1:
        Addr,Conn = Receiver.accept()
        Detail = Addr.recv(1024)
        FileReceiver(Addr,json.loads(Detail.decode()))
def FileReceiver(addr,detail):
    FileCont = b""
    try:
        os.mkdir(Directory)
        os.chdir(Directory)
    except FileExistsError:
        pass
    while 1:
        FileCont = addr.recv(1000000000)
        with open(detail["FileName"],"ab") as File:
            File.write(FileCont)
        if FileCont == b"":
            FileName = os.path.splitext(detail["FileName"])[0]
            os.rename(detail["FileName"],FileName+detail["FileExtension"])
            break
    print("Written Success")
Main()

