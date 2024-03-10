
if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(f'This is the {script_name} script. ' +
          """It takes in user credentials,
          quearies bank institutions\' API,
          and returns raw CSV data""")