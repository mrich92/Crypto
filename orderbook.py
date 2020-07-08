from client import Client
import json
import pandas as pd



class OrderBook_client(Client):
    def __init__(self, url, exchange, lock):
        super().__init__(url, exchange)
        self.lock = lock
        self.exchange = exchange
        self.DATA_DF = pd.DataFrame()


    def on_message(self, message):
        pass




