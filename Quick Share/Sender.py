import socket, os , threading , json
Sender = socket.socket()
Ip,Port = "127.0.0.1" , 9090
Sender.connect((Ip,Port))
FileName = "New.txt"
FileExt = ".py"
FilePath = "E:\\Quick Share\\v2\\tst.py"
Detail = {"FileName":FileName,"FileExtension":FileExt}
Sender.send(json.dumps(Detail).encode())
try:
    with open(FilePath,"rb") as File:
        FileCont = File.read()
        Sender.send(FileCont)
except FileNotFoundError:
    print("No File Found")