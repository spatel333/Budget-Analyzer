from pathlib import Path
import extract
import transform
import load
import subprocess
import csv


def main():
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')

    extract.main()
    transform.main()
    load.main()

    print("\n\n")
    print("Welcome to the menu. Let's check our data")
    login()
    print("")

def login():
    while(True):
        prompt = input("Want to update credentials? [y/n]: ")
        if prompt.lower() == 'y':
            grab_credentials()
        elif prompt.lower() == 'n':
            print("Using existing credentials")
            break



    ### TODO:
        # Make an API call to bank site
        # Acknowledge Successful Login
    msg = "Here we'd be implementing an API Call to the bank institution"
    [print('*') for i in len(msg)]
    print(msg)
    [print('*') for i in len(msg)]
    ###

    

    print("Login Complete!")


def grab_credentials():

    # open file in which we'll save credentials
    credentials_path = "./credentials.txt"
    subprocess.run(['touch', credentials_path])

    # prompt for credentials
    username = input("Username: ")
    password = input("Password: ")

    with open(credentials_path, 'w') as creds_file:
        creds_file.write(f'{username}\n{password}')







if __name__ == "__main__":
    main()