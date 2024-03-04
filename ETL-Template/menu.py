import extract, transform, load
import os
import csv


def main():
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')

    print("Welcome to the menu. Let's check our data")
    login()
    
    transform.main()

def login():
    credentials_path = "./credentials.txt"
    
    # check time of last credentials update & advise password change

    # if empty, prompy for creds
    username = input("Username: ")
    password = input("Password: ")

    with open(credentials_path) as credentials_file:
        credentials_file.writelines({"username": username,"Password": password})
        # credentials_file.wri








if __name__ == "__main__":
    main()