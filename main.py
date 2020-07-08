from exchange_clients import *
import threading

# urls..
binance_url = "wss://fstream.binance.com/ws/btcusdt@bookTicker"
ftx_url = "wss://ftx.com/ws/"
bitmex_url = "wss://www.bitmex.com/realtime"
trades_url = "wss://fstream.binance.com/stream?streams=btcusdt@aggTrade"

# Adding thread lock
lock = threading.Lock()

# Initializing websocket clients for each exchange
binance_orderbook = Binance_client(url=binance_url, exchange='binance', lock=lock)
ftx = Ftx_client(url=ftx_url, exchange='ftx',lock=lock)
bitmex = Bitmex_client(url=bitmex_url, exchange='bitmex',lock=lock)
binance_trades = Trades_client(url=trades_url, exchange='binance', lock=lock)

"""
## Each step of the proces is here to be run.
## Just comment out by each (part) to see see the results

# Book data (part 1 & 2) start..
# Part 2 needs an hour to cache enough data to print the "mid price"
"""
ftx.start()                       # Uncomment to run
bitmex.start()
binance_orderbook.start()

"""
 # Trades (Part 3) start
"""

# binance_trades.start()            # Uncomment to run


"""
# (Part 5)                      
"""
# binance_orderbook.start()             # Uncomment to run.
# binance_trades.start()
