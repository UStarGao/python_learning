#Author: UStarGao

import getpass

_username = 'UStarGao'
_password = '123456'
username = input("username:")
#password = getpass.getpass("password:")
password = input("password:")
if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")