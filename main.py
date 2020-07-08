from exchange_clients import *
import threading

# urls..
binance_url = "wss://fstream.binance.com/ws/btcusdt@bookTicker"
ftx_url = "wss://ftx.com/ws/"
bitmex_url = "wss://www.bitmex.com/realtime"

# Orderbook URL
book_url = "wss://fstream.binance.com/stream?streams=btcusdt@depth"

# Adding thread lock
lock = threading.Lock()

# Orderbook websocket client
orderbook = OrderBook_client(url=book_url, exchange='binance', lock=lock)

# Initializing websocket clients for each exchange
binance = Binance_client(url=binance_url, exchange='binance',lock=lock)
ftx = Ftx_client(url=ftx_url, exchange='ftx',lock=lock)
bitmex = Bitmex_client(url=bitmex_url, exchange='bitmex',lock=lock)




# Program start
ftx.start()
bitmex.start()
binance.start()








