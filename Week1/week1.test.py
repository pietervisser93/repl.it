import socket
import sys
import os
import subprocess


# noinspection PyBroadException
def messageRelay():
    global data
    global password
    HOST = ''  # Listen on all interfaces.
    PORT = 8888  # Assign port 8888
    Usernames = []
    Password = []

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

    try:
        # fetch username
        conn.sendall(b'Tell me your name first: ')
        while data != b'':
            data = conn.recv(1024)
            username = str(data.decode('ascii')).rstrip()


        # fetch password.
        conn.sendall(b'Type in a Password: \r\n\r\n')
        while password is b'':
            data = conn.recv(1024)
            password = str(data.decode('ascii')).rstrip()

    except:
        print('Couldnt catch username or password')

    try:
        # Give server information.
        conn.sendall(b'\r\nWelcome to the server ' + username.encode () + b'! \r\n\r\n')
        conn.sendall(b'Type something to me and I will respond with the same. \r\n')
        conn.sendall(b'Try launching an app through me, for example:\r\n')
        conn.sendall(b'Notepad, Calculator, Netflix.\r\n')
        conn.sendall(b'To stop type stop.\r\n\r\n')
        conn.sendall(b'Lets go!!!!:\r\n')
    except:
        print("Error giving server information.")

    while True:
        try:
            # Wait on input of client and return input (echo service)
            data = conn.recv(1024)
            data = str(data.decode('ascii')).rstrip()  # # Remove \r | \n | \r\n
            print('> Client data received: ' + data)
            conn.sendall(username.encode() + b': \r\n')

        except:
            print("No data or invalid data received")

        try:
            if data == "stop" or data == "Stop":
                print('> Client disconnected: ' + addr[0] + ':' + str(addr[1]))
                conn.sendall(b"Disconnecting from server :)")
                conn.close()
                s.close()

        except OSError as Err:
            print(Err)
            return

        try:
            if data == "notepad" or data == "Notepad":
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        except:
            print("Couldn't open Notepad")

        try:
            if data == "calculator" or data == "Calculator" or data == "Calc" or data == "calc":
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        except:
            print("Couldn't open calc")

        try:
            if data == "netflix" or data == "Netflix":
                os.system('start Netflix:')

        except:
            print("Couldn't open Netflix")


messageRelay()
