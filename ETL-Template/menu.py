import extract
import transform
import load
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






if __name__ == "__main__":
    main()