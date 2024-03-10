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

def login():

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