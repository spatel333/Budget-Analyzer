import subprocess

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
    query_site()

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

def query_site():
    # check for stored credentials
    # queary API
    site = "www.fakewebsite.com"
    print(f'{site}')



if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')
    [print(f'\t{x}') for x in locals().values() if callable(x)]