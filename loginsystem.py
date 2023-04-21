import os
clear = lambda: os.system('cls')
def main():
    clear()
    print("Main Menu")
    print("---------")
    print()
    print("1-Register")
    print("2-Login")
    print()
    while True:
        print()
        userChoice=input("Choose an option")
        if userChoice=='1' or userChoice=='2':
            break
    if userChoice=='1':
        register()
    else:
        login()

def register():
    clear()
    print("Register")
    print("--------")
    print()
    while True:
        userName= input("Enter your name: ").title()
        if userName!='':
            break 
    #userName= sanitizeName(userName)
    while True:
        userPassword= input("Enter Your Password: ")
        if userPassword !='':
            break
    while True:
        confirmPassword=input("confirm Your password: ")
        if confirmPassword==userPassword:
            break
        else:
            print("Password don't match")
            print()
    if userAlreadyExist(userName,userPassword):
        while True:
            print()
            error =input("You are already registered. \n\n press (T) to try again:\n press (l) to login:").lower()

            if error=='t':
                register()
                break
            elif error=='l':
                login()
                break
    addUserInfo([userName,userPassword])
    print()
    print("registered")

def login():
    clear
    print("Login")
    print("-----")
    print()
    """userInfo={}
    with open('userInfo.txt','r') as file:
        for line in file:
            line=line.split()
            userInfo.update({line[0]:line[1]})"""

    while True:
        f=0
        userName=input("Enter your name: ").title()
        userPassword=input("Enter your password ")
        #userName=sanitizeName(userName)
        with open('userInfo.txt','r') as file:
         for line in file:
            line=line.split(' ')
            if line[0]==userName and line[1]== userPassword:
                f=1
                break
         if f!=1:
           print("You are not registered or you are not loged in!")
           print()
        if f==1:
            break
    print()
    print("logged in !")
            
    '''if userName not in userInfo:
            print("You are not registered")
            print()
        else:

            userPassword=input("Enter your password ")
            if userPassword not in userInfo:
                print("Wrong Password")
                print()
            else:
                break'''       

def addUserInfo(userInfo:list):
    with open('userInfo.txt','a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')


def userAlreadyExist(userName,userPassword):
    userInfo={}
    with open('userInfo.txt','r') as file:
        for line in file:
            line=line.split(' ')
            if line[0]==userName and line[1]== userPassword:
                userInfo.update({line[0]:line[1]})
    if userInfo=={}:
        return False
    return userInfo[userName]==userPassword


main()