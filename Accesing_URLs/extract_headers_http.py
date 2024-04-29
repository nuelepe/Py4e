#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#http://data.pr4e.org/intro-short.txt

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address  = ("data.pr4e.org",80)
client_socket.connect(server_address)

#had to add the host part afer the blank lines.
request = "GET http://data.pr4e.org/intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n"
client_socket.send(request.encode())
print("Communication opened")

#The course condition would not be met and it kept cycling
while True:
    data = client_socket.recv(512)
    if not data:
        break
    print(data.decode())

client_socket.close()
print("Communication ended")