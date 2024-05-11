def main():
    # Introduction
    script_name = __file__.split('/')[-1]
    print(f'{script_name}')

    # Pull data from various sources
    graph1 = "Discover"
    graph2 = "Community Trust"


def query_site():

    ###TODO###
    # leverage Plaid to sign into bank institutions & pull transaction data
    # pull from specified banking platform
        # which dates?
        # which bank?
        # which account?
    
    client_id = "6605da1447127a001b95b1fb"
    
    return load_local_data()

def load_local_data():
    print("grab local .csv files")
    with open("../bank_statements/sample_data.csv", "r") as csv_file:
        
        ###TODO###
        print ("placeholder")





if __name__ == "__main__":
    main()