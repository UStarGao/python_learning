#Author:UStarGao 
_username = 'gao'  
_password = '123456'  
  
username = input("username:")  
password = input("password:")  
#判断语句  
if _username == username and _password == password:  
    print("Welcome user {name} login".format(name=username))  
else:  
    print("Invalid username or password")  
print(username,password)  
