import pandas as pd
from binance.client import Client

class Coin_Trader():
    def __init__(self):
        self.api_key = "l7CtfF68BY1N1w8vlBNkNyWGArbi0VvDEDhidkZCX3EKJVsJyklFBuqY47H83V3t"
        self.api_secret = "UktNpUtYhP29dfecFXbqweJFYU2IIG8YbVp79jePor6Lu1DkISelftBHqfaUAWWp"
        self.client = Client(api_key=self.api_key, api_secret=self.api_secret)
    
    def get_all_ticker(self):
        tickers = self.client.get_all_tickers()
        df = pd.DataFrame(data=tickers)
        df.set_index("symbol", inplace=True)
        print(df.head())
        
    def get_ticker(self, symb):
        tickers = self.client.get_all_tickers()
        df = pd.DataFrame(tickers)
        
        return df[df["symbol"] == symb]['price']
    
    def get_symbol_ticker(self, symb):
        pass
    
    def get_asset_balance(self, symb):
        pass
    
    def create_limit_buy(self, symb, price, qunt):
        pass
    
    def create_limit_sell(self, symb, price, qunt):
        pass
    
    def create_market_buy(self, symb, qunt):
        self.order = self.client.order_market_buy(
            symbol = symb,
            quntity = qunt
        )
        
        return self.order
    
    def create_market_sell(self, symb, qunt):
        self.order = self.client.order_market_sell(
            symbol = symb,
            quantity = qunt
        )
        
        return self.order
    

if __name__ == "__main__":
    trader = Coin_Trader()
    price = trader.get_ticker("BTCUSDT")
    print(price)