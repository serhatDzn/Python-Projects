import requests
url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"

def get_crpyo_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

crypto_response = get_crpyo_data()

user_input = input("Enter your cryptocurrency : ")

for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break