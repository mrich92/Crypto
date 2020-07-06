from client import Client
import json
import time

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