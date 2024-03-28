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
    # pull jackpot amount
    gross_winnings = pull_current_lotto_winnings()
    gross_winnings_as_currency = decimal_as_currency(gross_winnings)
    print(f'Congrats on winning {gross_winnings_as_currency}')
    
    # calculate taxes on gross winnings
    taxes, tax_breakdown = tax_winnings(gross_winnings)
    taxes_as_currency = decimal_as_currency(taxes)

    # print tax information
    print(f'You will pay {taxes_as_currency} in taxes')
    yes_responses = {'y', 'Y', 'yes', 'YES'}
    if input("Would you like a breakdown? [Y/n]: ") in yes_responses:
        [print(f'\t{key}:\t${value}') for key,value in tax_breakdown.items()]
    print("-------------------------------------")

    # print net winnings
    net_winnings_as_decimal = gross_winnings - taxes
    net_winnings_as_currency = decimal_as_currency(net_winnings_as_decimal)
    print(f'Your net winnings is {net_winnings_as_currency}')


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
    
    return round(amount_as_decimal, 2)
    

def decimal_as_currency(gross_winnings: int) -> str:
    
    #set locale data 
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')

    # convert to currency
    return locale.currency( gross_winnings, grouping=True)


def tax_winnings(amount) -> tuple:

    # calculate each taxation amount
    tax_breakdown = {}
    tax_breakdown['Federal'] = round(amount * Decimal(0.24), 2)
    tax_breakdown['State'] = round(amount * Decimal(0.05), 2)
    
    # calculate gross taxation amount
    taxes = tax_breakdown['Federal'] + tax_breakdown['State']

    return round(taxes, 2), tax_breakdown



if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(script_name)

    main()