import requests
from exchange_clients import Binance_client


class OrderBook():
    def __init__(self):
        self.ws_client = Binance_client()
        self.api_client = ''        # Add api call