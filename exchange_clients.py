from client import Client
import pandas as pd
from orderbook import OrderBook_client
import json
import time

DATA_DF = pd.DataFrame()
seconds_passed = {}
second_counter = 0

class Binance_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)
        self.lock = lock

    def on_message(self, message):
        global DATA_DF, seconds_passed, second_counter
        data = json.loads(message)
        data = {
            "timestamp": int(time.time()),
            "exchange": self.exchange,
            "market": data['s'],
            "bid_price": float(data['b']),
            "bid_size": float(data['B']),
            "ask_price": float(data['a']),
            "ask_size": float(data['A']),
            # "mid_price_1hour": (float(data['b'])+float(data['a'])) /2
        }

        if not data['timestamp'] in seconds_passed:
            seconds_passed[data['timestamp']] = True
            DATA_DF = DATA_DF.append(data, ignore_index=True)
            # DATA_DF = DATA_DF.set_index('timestamp')
            print(DATA_DF)

        if len(seconds_passed) >= 3:
            # val = (df.iloc[0]['bid_price']+df.iloc[0]['ask_price'])/2
            val = (DATA_DF.iloc[0]['bid_price']+DATA_DF.iloc[0]['ask_price'])/2
            DATA_DF = DATA_DF.iloc[0:]
            # data.update({"1_hour_midprice": val)



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
        global DATA_DF
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
        # Write to main dataframe
        # with self.lock:
        #     DATA_DF = DATA_DF.append(data, ignore_index=True)

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
        global DATA_DF
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

        # Write to main dataframe
        # with self.lock:
        #     DATA_DF = DATA_DF.append(data, ignore_index=True)

