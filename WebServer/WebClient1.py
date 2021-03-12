"""
Alessia De Giovannini
Web Client TCP 
"""
import requests

def client():
    url = 'http://127.0.0.1:5000'

    fileUser = open("Username.txt", "r")
    
    for User in fileUser:
        User = User.replace("\n", "")
        filePass = open("Password.txt", "r")
        for Pass in filePass: 
            Pass = Pass.replace("\n", "")
            param = {'username': User, 'password': Pass}
            x = requests.post(url, data = param)
            if "500 Internal Server Error" in x.text: 
                print(User + ": " + Pass + " corrette")
            else: 
                print(User + ": " + Pass + " errate")
                
    fileUser.close()
    filePass.close()

def main(): 
    client()

if __name__ == "__main__":
    main()