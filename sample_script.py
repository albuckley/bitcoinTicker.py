import BitcoinTicker as bt

## Print the latest price of each exchange

print "Coindesk Bitcoin Price Index: " + bt.coindeskBPI()
print "Bitfinex Last Price: " + bt.bitfinex()
print "CoinBase Last Price: " + bt.coinbase()
print "BTCE Last Price: " + bt.btce()
print "BitStamp Last Price: " + bt.bitStamp()
print "CampBX Last Price: " + bt.campBX()
print "Kraken Last Price: " + bt.kraken()
print "BTC China Last Price (Yuan): " + bt.btcChina()
print "OK Coin Last Price (Yuan): " + bt.OKCoin()
