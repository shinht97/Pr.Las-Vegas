import ChatBot as CB
import Coin_Trader as CT

if __name__ == "__main__":
    bot = CB.ChatBot()
    bot.send_message("메인 프로그램 활성화")
    
    trader = CT.Coin_Trader()
    
    price = trader.get_ticker("BTCUSDT")
    
    bot.send_message(f"비트 코인 현재 가격 : {price}")
    
    