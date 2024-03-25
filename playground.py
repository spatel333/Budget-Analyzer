import ast

queary_response = {}

queary_response['error'] = 420
queary_response['next_draw'] = 800000000
queary_response['currency'] = 'USD'
queary_response['jackpot'] = 750000000

# print(queary_response)

with open("jackpot_data.txt", "r+") as file:
    file.write(queary_response.__str__())
    ast.

# with open("jackpot_data.txt", "r") as jackpot_save_file:
#     print(jackpot_save_file.read())
#     file_as_json = json.load(jackpot_save_file)
#     # print(f'printing from file: {file_as_json}')
  