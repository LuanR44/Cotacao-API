import requests
from dotenv import load_dotenv
import os

load_dotenv()

class CurrencyConverter:
    def __init__(self):
        api_key = os.getenv('API_KEY')
        self.api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

    def convert(self, base_currency, target_currency, amount):
        response = requests.get(self.api_url + base_currency)
        data = response.json()

        if response.status_code != 200:
            raise Exception(f"A solicitação da API falhou e retornou o status {response.status_code}: {data.get('error-type')}")

        rates = data.get('conversion_rates', {})
        rate = rates.get(target_currency)

        if rate is None:
            raise Exception(f"Moeda {target_currency} não encontrada.")

        return amount * rate
