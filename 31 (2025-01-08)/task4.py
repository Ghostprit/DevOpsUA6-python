import requests

response = requests.get('https://api.coinbase.com/v2/prices/btc-usd/spot')
data = response.json()
print('Bitcoin current price (USD):', data['data']['amount'])