import re


def changePassword():
    while True:
        oldpassword = input("Enter your Old password:")
        newpasswd = input("Enter a new password: ")
        password = None
        if oldpassword == newpasswd:
            print("You cannot use the same password.")
            return False
        elif len(newpasswd) < 8:
            print("Make sure your password is atleast 8 letters.")
            return False
        elif re.search('[0-9]', newpasswd) is None:
            print("Make sure your password has a number in it.")
            return False
        elif re.search('[A-Z]', newpasswd) is None:
            print("Make sure your password has a capital letter in it.")
        else:
            password = newpasswd
            print("Your password changed.")
            return True

changePassword()