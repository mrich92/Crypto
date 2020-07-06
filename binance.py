from client import Client
import json
import time

class Binance_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)

        self.lock = lock

    def on_message(self, message):
        quote = json.loads(message)
        print({
            "timestamp": int(time.time()),
            "exchange": self.exchange,
            "market": quote['s'],
            "bid_price": quote['b'],
            "bid_size": quote['B'],
            "ask_price": quote['a'],
            "ask_size": quote['A'],
        })