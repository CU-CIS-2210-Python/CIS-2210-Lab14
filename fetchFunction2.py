import socket
import json

#This function performs an HTTP fetch of the given file from the
#hostname specified. It RETURNS the contents.
def fetch(hostName, fileName):
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
        stream.readline().rstrip()

        #Step 2️⃣:Read line by line...
        for line in stream:
            if line == "\n": #If it is a blank line...
                break        #Stop reading headers

        #Step 3️⃣: After the blank line at the end of the headers
        #comes the contents, which continues to the end.
        contents = ""
        for line in stream:
            contents = contents + line

        return contents

text = fetch("lab14.billkuker.com", "/data/squad.json")

data = json.loads(text)

print("breakpoint here")

print(data['members'][1]['name'])