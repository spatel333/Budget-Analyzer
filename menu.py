import extract.extract as extract
import transform.transform as transform
import load.load as load
import csv


def main():
    extract.main()
    transform.main()
    load.main()

    print("\n\n")
    print("Welcome to the menu. Let's check our data")
    extract.login()



if __name__ == "__main__":
    # main()
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')
    [print(f'\t{x}') for x in locals().values() if callable(x)]
    # [print(x) for x in locals().items()]