#We will write python code do download the following data:
#http://lab14.billkuker.com/data/squad.json

import socket

hostName = "lab14.billkuker.com"
fileName = "/data/story.txt"

#Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostName, 80))

    #Convert the connection into a stream we can read and write
    stream = s.makefile("rw")

    #Make an HTTP Request
    stream.write(f"GET {fileName} HTTP/1.0\n")
    stream.write(f"Host: {hostName}\n")
    stream.write("\n")
    stream.flush()

    #Read the HTTP Response...

    #Step 1️⃣: Read the first line, which is the STATUS
    status = stream.readline().rstrip()
    print(f"== HTTP Status: {status}")

    #Step 2️⃣: Each subsequent line is a HEADER. Headers are
    #formatted as a name, a colon and space, and a value:
    #HeaderName: HeaderValue
    #After the last header is a BLANK LINE

    #Create a dictionary to keep the headers in
    headers = {}
    #Read line by line...
    for line in stream:
        if line == "\n": #If it is a blank line...
            break        #Stop reading headers
        #Split into two parts at the ": "
        split = line.rstrip().split(": ", 2)
        #And add them to the dicttionary
        headers[split[0]] = split[1]

    #Print out the headers fromt the server...
    print("== HTTP Headers ==")
    for (name, value) in headers.items():
        print(f"\t{name}: {value}")

    #Step 3️⃣: After the blank line at the end of the headers
    #comes the contents, which continues to the end.
    contents = ""
    for line in stream:
        contents = contents + line

    print("== HTTP Content ==")
    print(contents)