import typer
import os
import sys
import platform
import time
import inquirer

class NotUsingWindows(Exception):
    pass

class UnsupportedEdition(Exception):
    pass

# Define the product keys dictionary
product_keys = {
    'home': 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
    'pro': 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
    'education': 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
    'enterprise': 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
    'professional': 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
}

def crack(edition):
    edition = edition.lower()
    if edition in product_keys:
        product_key = product_keys[edition]
        os.system(f"slmgr /ipk {product_key}")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")

if platform.system() == 'Windows':
        edition = platform.win32_edition()
        if edition and (edition == "Home" or edition == "Pro" or edition == "Professional" or edition == "Enterprise" or edition == "Education"):
            pass
        else:
            raise UnsupportedEdition("The edition of your Windows is not supported by this program.")
            sys.exit()
else:
        raise NotUsingWindows("You are not on Windows, this script is only for Windows.")
        sys.exit()

app = typer.Typer()

@app.command()
def manual(edition: str):
    restartQ = [inquirer.List('restart', message="Would you prefer to restart now to apply changes?",choices=['Sure', 'Not now'],),]
    edition = edition.lower()
    edit = edition.capitalize()
    if(not(edition == "home" or edition == "pro" or edition == "professional" or edition == "enterprise" or edition == "education")):
        raise UnsupportedEdition("Invalid edition or it does not exist.")
        print("Try Home, Pro, Professional, Education or Enterprise. Also spell correctly and completely.")
    print(f"Attempting to crack the {edit} Edition.")
    crack(edition)
    print("The dialogs should have told you whether it was success or no.")
    print("If it required permissions, open command prompt as adminstrator and then run the python file to work.")
    restartQ = inquirer.prompt(restartQ)
    if(restartQ["restart"] == "Sure"):
        print("Ok, restarting in 30 seconds. Save your work if you haven't!")
        time.sleep(30)
        os.system("shutdown /s /f /t 0")

@app.command()
def automatic():
    restartQ = [inquirer.List('restart', message="Would you prefer to restart now to apply changes?",choices=['Sure', 'Not now'],),]
    edition = (platform.win32_edition()).lower()
    crack(edition)
    print("The dialogs should have told you whether it was success or no.")
    print("If it required permissions, open command prompt as adminstrator and then run the python file to work.")
    restartQ = inquirer.prompt(restartQ)
    if(restartQ["restart"] == "Sure"):
        print("Ok, restarting in 30 seconds. Save your work if you haven't!")
        time.sleep(30)
        os.system("shutdown /s /f /t 0")

if __name__ == "__main__":
    app()