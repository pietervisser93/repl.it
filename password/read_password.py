import re
import hashlib

passPath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\password\\password.txt"


def readPassword():
    fileRead = open(passPath, "r")
    password = input(str('Fill in your password: '))
    passwordBytes = str.encode(password)
    password = hashlib.sha256(passwordBytes).hexdigest()
    lines = fileRead.readlines()
    print(lines)
    for line in lines:
        print(line)
        if password in line:
            print("Wachtwoord Ok")
        else:
            print("Wachtwoord Fout")
    fileRead.close()


readPassword()



