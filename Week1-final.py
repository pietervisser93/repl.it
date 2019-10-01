import socket
import sqlite3
import sys
import os
import subprocess
import webbrowser
import time, os, fnmatch, shutil

# noinspection PyBroadException
def messageRelay():
    global data
    global password
    global username
    logPath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\log.txt"
    HOST = ''  # Listen on all interfaces.
    PORT = 8888  # Assign port 8888
    usernameList = []
    passwordList = []
    t = time.localtime()
    timestamp = time.strftime('%d-%b-%Y %H:%M', t)

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

    # try:
    #     # Openb database
    #     connenction = sqlite3.connect('C:\\Users\\Home\\PycharmProjects\\PiPos-Nsapi\\NS_API\\db.db2')
    #     c1 = connection.cursor()
    #
    # except:
    #     print('Couldnt open the database')

    conn.sendall(b'Tell me your name first: \r\n')

    try:
        while True:
            # Fecth users name
            data = conn.recv(1024)
            data = str(data.decode('ascii')).rstrip()
            print(data)
            if data != b'':
                username = data
                if username not in usernameList:
                        usernameList.append(username)
                        print('User not found creating user: ' + username)
                        print(usernameList)
                        break
    except:
        conn.sendall(b'Something went wrong with filling in your username\r\n')

    logwrite = open(logPath, "a")
    log = timestamp + ' > ' + username + ' connected with: ' + addr[0] + ':' + str(addr[1]) + '\r\n'
    logwrite.writelines(log)
    logwrite.close()

    try:
        # Give server information.
        conn.sendall(b'\r\nWelcome to the server ' + username.encode() + b'! \r\n\r\n')
        conn.sendall(b'Type something to me and I will respond with the same. \r\n')
        conn.sendall(b'Try launching an app through me, for example:\r\n')
        conn.sendall(b'Notepad, Calculator, Netflix.\r\n')
        conn.sendall(b'To stop type stop.\r\n\r\n')
        conn.sendall(b'Lets start: \r\n')

    except:
        print('Giving server information went wrong :\'(')
        conn.sendall(b'Giving server information went wrong :\'(\r\n')

    while True:
        if username in usernameList:
            try:
                # Wait on input of client and return input (echo service)
                if data != b'':  # and data != '' and data != ' ' and data != '' and data is not None:
                    print('> Client data received: ' + str(data))
                    conn.sendall(username.encode() + b': ')
                    data = conn.recv(1024)
                    data = str(data.decode('ascii')).rstrip()  # # Remove \r | \n | \r\n
                    print("data: " + data)
                else:
                    print("blank line")

            except:
                print("No data or invalid data received")

            try:
                if data == "stop" or data == "Stop":
                    logwrite = open(logPath, "a")
                    log = timestamp + ' > ' + username + ' disconnected: ' + addr[0] + ':' + str(addr[1]) + '\r\n'
                    logwrite.writelines(log)
                    logwrite.close()
                    print(timestamp + ' > ' + username + ' disconnected: ' + addr[0] + ' @ ' + str(addr[1]))
                    conn.sendall(b"Disconnecting from server :)")
                    conn.close()
                    s.close()

            except OSError as Err:
                print(Err)
                return

            try:
                if data == "notepad" or data == "Notepad":
                    logwrite = open(logPath, "a")
                    log = timestamp + " > " + username + ' started: Notepad\r\n'
                    logwrite.writelines(log)
                    logwrite.close()
                    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

            except:
                print("Couldn't open Notepad")

            try:
                if data == "calculator" or data == "Calculator" or data == "Calc" or data == "calc":
                    logwrite = open(logPath, "a")
                    log = timestamp + " > " + username + ' started: Calculator\r\n'
                    logwrite.writelines(log)
                    logwrite.close()
                    subprocess.Popen('C:\\Windows\\System32\\calc.exe')

            except:
                print("Couldn't open calc")

            try:
                if data == "netflix" or data == "Netflix":
                    logwrite = open(logPath, "a")
                    log = timestamp + " > " + username + ' started: Netflix\r\n'
                    logwrite.writelines(log)
                    logwrite.close()
                    os.system('start Netflix:')

            except:
                print("Couldn't open Netflix")

        else:
            print("User not authenticated!")

            # try:
            #     if data == "Pornhub" or data == "pornhub" or data == 'ph':
            #         # chrome_cmd = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
            #         edge_cmd = "C:\\Windows\\SystemApps\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\MicrosoftEdge.exe %s"
            #         a_website = "www.porhub.com"
            #         webbrowser.get(edge_cmd).open_new(a_website)
            #
            # except:
            #     print("Couldn't open Pornhub")


messageRelay()

