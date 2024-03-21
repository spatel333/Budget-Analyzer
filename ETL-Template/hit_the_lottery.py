"""
WE HIT THE JACKPOT!!!! WOOHOO!!!
Now the question is... where do we put this money?
"""

def main():
    amount = pull_current_lotto_winnings()
    taxes = pull_taxation(amount)

def pull_current_lotto_winnings():
    return 1

def pull_taxation(amount):
    return amount*0.2



if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(script_name)