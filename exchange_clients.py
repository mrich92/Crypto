
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

class Bitmex_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)

        self.lock = lock
        self.exchange = exchange


    def on_open(self):
        super().on_open()
        payload = {
            "op": "subscribe",
            "args": [
                "quote:XBTUSD"
            ]
        }

        self.ws.send(json.dumps(payload))

    def on_message(self, message):
        data = json.loads(message)
        # print(data)
        print({
            'timestamp': int(time.time()),
            "exchange": self.exchange,
            'market': data['data'][-1]['symbol'],
            'bid': data['data'][-1]['bidPrice'],
            'bidSize': data['data'][-1]['bidSize'],
            'ask': data['data'][-1]['askPrice'],
            'askSize': data['data'][-1]['askSize']
        })
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

