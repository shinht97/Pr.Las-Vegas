import datetime
import requests

class ChatBot():
    def __init__(self):
        self.DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1202205261016875059/Wqxnj3Bg8IzwH688p8QOdtIkjnuvW2thC8zM__7kKPG9RkQge_YX-UBjhKijRYvvx_HG'
        self.send_message("코인 알림 봇 대기중....")
        
    def send_message(self, msg):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        message = {
            "content" : f"[{now}] {str(msg)}"
        }
        
        requests.post(self.DISCORD_WEBHOOK_URL, data=message)
        
        print(message)
        
        
if __name__ == "__main__":
    bot = ChatBot()
    
    bot.send_message("안녕하세요 코인 알림 봇 입니다.")