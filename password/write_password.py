import re
import hashlib

# 2.3.3.2 Hoofdletter X #
passPath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\password\\password.txt"


def writePassword():
    fileWrite = open(passPath, "a")
    password = input(str('Fill in your password: '))
    passwordBytes = str.encode(password)
    password = hashlib.sha256(passwordBytes).hexdigest()
    fileWrite.writelines(password + '\r\n')
    fileWrite.close()


writePassword()
