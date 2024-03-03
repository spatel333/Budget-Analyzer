import extract
import transform
import load

def main():
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')

    print("Welcome to the menu. Let's check our data")
    login()
    
    transform.main()

def login():
    credentials_file = "/path/to/file"
    
    # check time of last credentials update & advise password change

    # if empty, prompy for creds
    # username = input("Username")
    # password = input("Password")





if __name__ == "__main__":
    main()