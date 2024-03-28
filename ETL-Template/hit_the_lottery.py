import requests
import locale
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
"""
WE HIT THE JACKPOT!!!! WOOHOO!!!
Now the question is... where do we put this money?
"""

def main():
    gross_winnings = pull_current_lotto_winnings()
    print(f'Gross Winnings: {gross_winnings}')

    gross_winnings_as_currency = winnings_as_currency(gross_winnings)
    print(f'Congrats on winning {gross_winnings_as_currency}')
    # taxes = pull_taxation(gross_winnings)

def pull_current_lotto_winnings() -> Decimal:
    # url = "https://data.ny.gov/resource/d6yy-54nr.json"
    
    # pull webpage
    url = "https://www.magayo.com/lotto/usa/powerball-results/"
    response = requests.get(url)
    
    # scrape webpage for jackpot data
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find(class_="col-lg")

    # convert jackpot from currency to decimal value
    amount_as_currency = results.text[results.text.find('$'):]
    amount_as_decimal = Decimal(sub(r'[^\d.]', '', amount_as_currency))
    
    return amount_as_decimal
    

def winnings_as_currency(gross_winnings: int) -> str:
    
    #set locale data 
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')

    # convert to currency
    return locale.currency( gross_winnings, grouping=True)



def pull_taxation(amount):
    return amount*0.2



if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(script_name)

    main()