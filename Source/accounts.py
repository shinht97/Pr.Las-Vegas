import ccxt

with open("./api.txt") as file:
    lines = file.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()
    
binance = ccxt.binance(config = {
    "apiKey" : api_key,
    "secret" : secret
    })

balance = binance.fetch_balance()

print(balance["BTC"])