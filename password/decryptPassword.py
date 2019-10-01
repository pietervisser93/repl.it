import hashlib
from itertools import product, chain
from tkinter import *
from tkinter.messagebox import showinfo

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # chars to look for
p = "3308B1A5C97FC05FCEC2973B3D5C2EE44C0A1D32CC4C23A367374CBD14A9ADBD"  # hash to crack
passPath = r"C:\\Users\\Home\\PycharmProjects\repl.it\\password\\password.txt"


def bruteforce():
    for i in range(1000):
            for length in range(1, 4):  # only do lengths of 1 to 3
                to_attempt = product(chars, repeat=length)  #
                for attempt in to_attempt:
                    print(''.join(attempt))
                    ww = str(attempt)
                    password = hashlib.sha256(ww.encode()).hexdigest()
                    if password is not p:
                        print('That wasnt the correct password! password was: ', password)
                        i = i+1
                        print(i, '\r\n')

                    else:
                        print('That was the correct password! password was: ', ww)
                        showinfo(title='Password found!: ', message=ww)
                        fileWrite = open(passPath, "r")
                        fileWrite.writelines(password + ww)
                        fileWrite.close()
                        break


bruteforce()
