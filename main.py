from exchange_clients import *
import threading

# urls..
binance_url = "wss://fstream.binance.com/ws/btcusdt@bookTicker"
ftx_url = "wss://ftx.com/ws/"
bitmex_url = "wss://www.bitmex.com/realtime"

# Adding thread lock
lock = threading.Lock()

# Initializing websocket clients for each exchange
binance = Binance_client(url=binance_url, exchange='binance',lock=lock)
ftx = Ftx_client(url=ftx_url, exchange='ftx',lock=lock)
bitmex = Bitmex_client(url=bitmex_url, exchange='bitmex',lock=lock)



# exchange_list = [binance, ftx, bitmex]
# for connection in exchange_list:
#     connection.start()
#
# bitmex.start()
# binance.start()
# ftx.start()


binance.start()








