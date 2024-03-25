def main():
    script_name = __file__.split('/')[-1]

    print(f'{script_name}')


def query_site():

    ###TODO###
    # leverage Plaid to sign into bank institutions & pull transaction data
    # pull from specified banking platform
        # which dates?
        # which bank?
        # which account?
    
    return load_local_data()

def load_local_data():
    print("grab local .csv files")
    with open("../bank_statements/sample_data.csv", "r") as csv_file:
        
        ###TODO###
        print ("placeholder")





if __name__ == "__main__":
    main()