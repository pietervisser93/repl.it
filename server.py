import socket
import sys
import subprocess

global s, data, conn


def messageRelay():
    global s, data, conn, addr
    HOST = ''  # Listen on all interfaces.
    PORT = 8888  # Assign port 8888

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(10)
        print('> Socket listening on Port:', PORT)

    except socket.error as err:
        print("socket creation failed with error %s" % err)

    try:
        # Waiting on connection (blocking)
        conn, addr = s.accept()

        # Client connected
        print('> Connected with: ' + addr[0] + ':' + str(addr[1]))

    except socket.gaierror:
        print("There was an error connecting")

    # Server reports back to client
    conn.sendall(b'Welcome to the server\r\n\r\n')
    conn.sendall(b'Tell me something: ')

    while True:
        try:
            # Wait on input of client and return input (echo service)
            data = conn.recv(1024)
            data = str(data.decode('ascii')).rstrip("\r\n")  # # Remove \r | \n | \r\n
            print('> Client data received: ' + data)

        except:
            print("No data or invalid data received")

        try:
            if data == "" or data == " ":
                conn.sendall(b"please dont leave your input empty\r\n")
            else:
                conn.sendall(b'You told me: ' + data.encode() + b"\r\n")

            # if data != " " or data != "":
              #  conn.sendall(b"You told me: " + data.encode())
                #conn.sendall(b'\r\n')

            # if data == " ":
            #   print("Users input was empty")
            #   conn.sendall(b"please dont leave your input empty\r\n")

            #if data == "":
            #   print("Users input was empty")
            #   conn.sendall(b"please dont leave your input empty\r\n")


        except:
            print("No valid input!")
            conn.sendall(b"No valid input")

        try:
            if data == "stop":
                print('> Client disconnected: ' + addr[0] + ':' + str(addr[1]))
                conn.sendall(b"Disconnecting from server :)")
                conn.close()
                s.close()

        except OSError as Err:
            print(Err)
            return


messageRelay()




