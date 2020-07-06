from ftx import Ftx_client
from bitmex import Bitmex_client
from binance import Binance_client
import threading


# urls..
binance_url = "wss://fstream.binance.com/ws/btcusdt@bookTicker"
ftx_url = "wss://ftx.com/ws/"
bitmex_url = "wss://www.bitmex.com/realtime"

lock = threading.Lock()

binance = Binance_client(url=binance_url, exchange='binance',lock=lock)
ftx = Ftx_client(url=ftx_url, exchange='ftx',lock=lock)
bitmex = Bitmex_client(url=bitmex_url, exchange='bitmex',lock=lock)


lis = [binance, ftx, bitmex]
for item in lis:
    item.start()














