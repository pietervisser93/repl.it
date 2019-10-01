# try:
#     # fetch username
#     print(usernameList)
#     print(username)
#     conn.sendall(b'Tell me your name first: ')
#     while username == b'' and username == b' ' and username not in usernameList and username is None:
#         data = conn.recv(1024)
#         username = str(data.decode('ascii')).rstrip()
#         usernameList.append(password)
#         usernameList.append(data)
#     print(usernameList)
#     print(username)
#
#     # fetch password.
#     conn.sendall(b'Type in a Password: \r\n\r\n')
#     print(passwordList)
#     print(password)
#     while password == b'' and password == b' ' and password not in passwordList and password is None:
#         data = conn.recv(1024)
#         password = str(data.decode('ascii')).rstrip()
#         passwordList.append(password)
#         passwordList.append(data)
#         print(passwordList)
#         print(password)
#
# except:
#     print('Couldnt catch username or password')


log = open(r"C:\\Users\\Home\\PycharmProjects\repl.it\\log.txt")


'> Connected with: ' + addr[0] + ':' + str(addr[1])