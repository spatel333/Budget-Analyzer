import requests
import locale
import subprocess
import json
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

def pull_current_lotto_winnings():
    # url = "https://data.ny.gov/resource/d6yy-54nr.json"
    
    url = "https://www.magayo.com/api/jackpot.php"
    api_key = "api_key=XSCztE26Ei97YzYMrA"
    field = "game=us_powerball"
    response = requests.get(f'{url}?{api_key}&{field}')
    data = response.json()

    if data['error'] == 303:
        print('API query limit reached')
        with open("jackpot_data.txt", "r") as jackpot_save_file:
            file_as_json = json.load(jackpot_save_file.read())
            print(f'printing from file: {file_as_json}')
        return -1
    else:
        print('Limit not reached')
        # subprocess.Popen([f'echo {data} > jackpot_data.txt'], shell=True)
        to_be_saved = {}
        to_be_saved['error'] = data['error']
        to_be_saved['next_draw'] = data['next_draw']
        to_be_saved['currency'] = data['currency']
        to_be_saved['jackpot'] = data['jackpot']
        with open("jackpot_data.txt", "w") as jackpot_save_file:
            jackpot_save_file.write(to_be_saved.__str__())

        return
        

    # response = {'error': 303, 'next_draw': '', 'currency': 'USD', 'jackpot': ''}

def winnings_as_currency(gross_winnings: int) -> str:
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    print(f'value: {gross_winnings}')
    s = locale.currency(gross_winnings, grouping=True)
    print(s)

    return locale.currency( gross_winnings, grouping=True)



def pull_taxation(amount):
    return amount*0.2



if __name__ == "__main__":
    script_name = __file__.split('/')[-1]
    print(script_name)

    main()