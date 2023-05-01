import socket

#Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("www.example.com", 80))

    #Convert the connection into a stream we can read and write
    stream = s.makefile("rw")

    #Make an http request
    stream.write("GET / HTTP/1.0\n")
    stream.write("Host: www.example.com\n")
    stream.write("\n")
    stream.flush()

    for line in stream.readlines():
        print(line.rstrip())