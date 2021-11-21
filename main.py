import os
import time
print("Windows Activator 1.3.5")
print("Type -help for help to how to activate windows for free & for more commands.")
def init():
    c = input("> ")
    if c == "pro":
        os.system("Pro.py")
    elif c == "education":
        os.system("Education.py")
    elif c == "enterprise":
        os.system("Enterprise.py")
    elif c == "home":
        os.system("Home.py")
    elif c == "professional":
        os.system("Professional.py")
    elif c == "pron":
        os.system("Pron.py")
    elif c == "homen":
        os.system("homen.py")
    elif c == "enterprisen":
        os.system("enterprisen.py")
    elif c == "educationn":
        os.system("educationn.py")
    elif c == "professionaln":
        os.system("professionaln.py")
    elif c == "professional":
        os.system("Professional.py")
    elif c == "exit()":
        exit()
    elif c == "":
        n = ""
    elif c == "help" or c == "help()":
        print("Type -help for interactive help.")
    elif c == "uninstall":
        def upk():
            f = input("Are you sure you want to uninstall current product key? Y/N")
            if f == "Y" or f == "y":
                print("Uninstalling Product key...")
                time.sleep(0.6)
                os.system("slmgr /upk")
                time.sleep(0.6)
                print("Product Key Uninstalled Successfully.")
            elif f == "N" or f == "n":
                init()
            else:
                print("Invalid choice. Try again!")
                upk()
        upk()
    elif c == "-help":
        print("-------------------- Windows Activator 1.3.5 --------------------")
        print("Type Home to activate windows as Home edition.")
        print("Type Pro to activate windows as pro edition.")
        print("Type Professional to activate windows as Professional edition.")
        print("Type Enterprise to activate windows as Enterprise edition.")
        print("Type Education to activate windows as Education edition.")
        print("Type Homen to activate windows as Home N edition.")
        print("Type Pron to activate windows as pro N edition.")
        print("Type Professionaln to activate windows as Professional N edition.")
        print("Type Enterprisen to activate windows as Enterprise N edition.")
        print("Type Educationn to activate windows as Education N edition.")
        print("Type Uninstall to De-activate Windows.")
        print("\nIf any errors were occured, try using no capital letters.")
        print("\nUse exit() to close.")
        print("\nStill having queries? Mail the owner of this at code.with.aasheesh@gmail.com")
    else:
        print("Can't run command of null.")
        print("Type -help to know how to activate.")
    init()
init()
