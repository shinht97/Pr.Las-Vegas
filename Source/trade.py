import ccxt
import pprint

with open("./api.txt") as file:
    lines = file.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()
    
binance = ccxt.binance(config = {
    "apiKey" : api_key,
    "secret" : secret
    })

order = binance.create_market_sell_order(
    symbol = "BTC/USD",
    amount = 0
)

pprint.pprint(order)