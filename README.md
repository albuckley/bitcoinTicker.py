# Bitcoin Ticker

bitcoinTicker.py. A Python script that helps you grab the latest bitcoin prices from top exchanges.

## Installation: 
Include the following line somewhere in your python file to import the script.
```python
import bitcoinTicker
```


## Available Functions:
Each of the following functions returns a string with the latest USD or Yuan (noted below) value of one Bitcoin on the given exchange or price index. The functions are named after the excanhges, be careful of exchanges with similar sounding names.

* coindeskBPI()
* bitfinex()
* coinbase()
* mtGox()
* btce()
* crypto_trade()
* bitStamp()
* campBX()
* kraken()
* OKCoin()
* btcChina()


## Usage:
The following is a simple script that includes the bitcoinTicker.py and then prints the latest prices.

```python
import bitcoinTicker as bt

## Print the latest price of each exchange
print "Coindesk Bitcoin Price Index: " + bt.coindeskBPI()
print "Bitfinex Last Price: " + bt.bitfinex()
print "CoinBase Last Price: " + bt.coinbase()
print "Mt.Gox Last Price: " + bt.mtGox()
print "BTCE Last Price: " + bt.btce()
print "Crypto Trade Last Price: " + bt.crypto_trade()
print "BitStamp Last Price: " + bt.bitStamp()
print "CampBX Last Price: " + bt.campBX()
print "Kraken Last Price: " + bt.kraken()
print "BTC China Last Price (Yuan): " + bt.btcChina()
print "OK Coin Last Price (Yuan): " + bt.OKCoin()

```

Output:
```
Coindesk Bitcoin Price Index: 609.4850
Bitfinex Last Price: 610.9901
CoinBase Last Price: 614.8389999999999
Mt.Gox Last Price: 135.00000
BTCE Last Price: 606.88
Crypto Trade Last Price: 610.019
BitStamp Last Price: 610.21
CampBX Last Price: 635.00
Kraken Last Price: 611.01000
BTC China Last Price (Yuan): 3712.00
OK Coin Last Price (Yuan): 3702.86
[Finished in 32.9s]
```

