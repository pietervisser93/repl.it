import socket
import sys
import subprocess


def messageRelay():
    HOST = ''  # Listen on all interfaces.
    PORT = 8888  # Assign port 8888
    Usernames = []
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
    conn.sendall(b'Tell me your name first: ')
    data = conn.recv(1024)
    username = str(data.decode('ascii')).rstrip()
    print("> Username:" + username)
    conn.sendall(b'Welcome to the server ' + username.encode() + b'! \r\n')
    conn.sendall(b'Type something to me and I will respond with the same. \r\n')
    conn.sendall(b'Try launching an app through me, to stop type stop.\r\n\r\n')

    while True:
        try:
            # Wait on input of client and return input (echo service)
            data = conn.recv(1024)
            data = str(data.decode('ascii')).rstrip()  # # Remove \r | \n | \r\n
            print('> Client data received: ' + data)

        except:
            print("No data or invalid data received")

        try:
            if data == "":
                print("Ignoring empty input")
            else:
                conn.sendall(b'You told me: ' + data.encode() + b"\r\n")

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

        except:
            print("Something else went wrong")


messageRelay()


def openApps():
    try:
        if data == "notepad":
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    except:
        print("Couldnt open Notepad")

    try:
        if data == "Notepad":
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    except:
        print("Couldnt open Notepad")


openApps()


