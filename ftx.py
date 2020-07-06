from client import Client
from datetime import datetime
import json


class Ftx_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)

        self.lock = lock

    def on_open(self):
        super().on_open()
        message = json.dumps({
            "channel": "ticker",
            "market": "BTC-PERP",
            "op": "subscribe"})
        self.ws.send(message)

    def on_message(self, message):

        quote = json.loads(message)
        print({
            "timestamp": int(quote['data']['time']),
            "exchange": self.exchange,
            "market": quote['market'],
            "bid_price": quote['data']['bid'],
            "bid_size": quote['data']['bidSize'],
            "ask_price": quote['data']['ask'],
            "ask_size": quote['data']['askSize'],
        })

