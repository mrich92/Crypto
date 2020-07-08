from client import Client
import json
import time

#  Binance cahce
binace_seconds_passed = {}
binance_cache = []

# Bitmex cache
bitmex_seconds_passed = {}
bitmex_cache = []

#  Ftx cache
ftx_seconds_passed = {}
ftx_cache = []

class Binance_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)
        self.lock = lock

    def on_message(self, message):
        global binance_seconds_passed, binance_cachecache
        data = json.loads(message)
        data = {
            "timestamp": int(time.time()),
            "exchange": self.exchange,
            "market": data['s'],
            "bid_price": float(data['b']),
            "bid_size": float(data['B']),
            "ask_price": float(data['a']),
            "ask_size": float(data['A']),
        }

        if not data['timestamp'] in binace_seconds_passed:
            binance_seconds_passed[data['timestamp']] = True
            binance_cache.append(data)
            print(binance_cache[-1])

        if len(binace_seconds_passed) >= 3600:                     # 3600 seconds == 1 hour..
            val = binance_cache.pop(0)                           # Remove value 3600 seconds ago..
            mid = (val['bid_price']+val['ask_price'])/2     # Compute hour ago mid price
            data.update({"mid_price_1H": mid})
            print(data)


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
        global bitmex_seconds_passed, bitmex_cache

        # Load message into dict
        data = json.loads(message)
        data = {
            'timestamp': int(time.time()),
            "exchange": self.exchange,
            'market': data['data'][-1]['symbol'],
            'bid': data['data'][-1]['bidPrice'],
            'bidSize': data['data'][-1]['bidSize'],
            'ask': data['data'][-1]['askPrice'],
            'askSize': data['data'][-1]['askSize']
        }
        if not data['timestamp'] in bitmex_seconds_passed:
            bitmex_seconds_passed[data['timestamp']] = True
            bitmex_cache.append(data)
            print(bitmex_cache[-1])

        if len(bitmex_seconds_passed) >= 3600:                     # 3600 seconds == 1 hour..
            val = bitmex_cache.pop(0)                           # Remove value 3600 seconds ago..
            mid = (val['bid_price']+val['ask_price'])/2     # Compute hour ago mid price
            data.update({"mid_price_1H": mid})
            print(data)


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
        global ftx_seconds_passed, ftx_cache

        data = json.loads(message)
        data = {
            "timestamp": int(data['data']['time']),
            "exchange": self.exchange,
            "market": data['market'],
            "bid_price": data['data']['bid'],
            "bid_size": data['data']['bidSize'],
            "ask_price": data['data']['ask'],
            "ask_size": data['data']['askSize'],
        }
        if not data['timestamp'] in ftx_seconds_passed:
            ftx_seconds_passed[data['timestamp']] = True
            ftx_cache.append(data)
            print(ftx_cache[-1])

        if len(ftx_seconds_passed) >= 3600:                     # 3600 seconds == 1 hour..
            val = ftx_cache.pop(0)                           # Remove value 3600 seconds ago..
            mid = (val['bid_price']+val['ask_price'])/2     # Compute hour ago mid price
            data.update({"mid_price_1H": mid})
            print(data)


class OrderBook_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)
        self.lock = lock
        self.exchange = exchange


    def on_message(self, message):
        pass
