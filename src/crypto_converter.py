import requests

class CryptoConverter:
    def __init__(self):
        self.api_url = 'https://api.coingecko.com/api/v3/'

    def convert(self, amount, base_currency, crypto_currency):
        price = self.get_price(crypto_currency, base_currency)
        return amount / price

    def get_price(self, crypto_currency, target_currency):
        response = requests.get(self.api_url + f'simple/price?ids={crypto_currency}&vs_currencies={target_currency}')
        data = response.json()

        if not data:
            raise Exception("Currency not found or API request failed")

        price = data.get(crypto_currency, {}).get(target_currency)

        if price is None:
            raise Exception(f"Currency {target_currency} not found")

        return price
