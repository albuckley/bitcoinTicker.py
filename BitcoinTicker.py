import json
import urllib2


def coindeskBPI():
	data = json_to_dict(get_URL('http://api.coindesk.com/v1/bpi/currentprice.json'))
	return data['bpi']['USD']['rate']

def btcChina():
	data = json_to_dict(get_URL('https://data.btcchina.com/data/ticker'))
	return data['ticker']['last']

def OKCoin():
	data = json_to_dict(get_URL('https://www.okcoin.com/api/ticker.do'))
	return data['ticker']['last']

def bitfinex():
	data = json_to_dict(get_URL('https://api.bitfinex.com/v1/ticker/btcusd'))
	return data['last_price']

def coinbase():
	#appears to update once per minute.
	data = json_to_dict(get_URL('https://coinbase.com/api/v1/currencies/exchange_rates'))
	return data['btc_to_usd']

def mtGox():
	data = json_to_dict(get_URL('http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast'))
	return data['data']['last']['value']

def btce():
	data = json_to_dict(get_URL('https://btc-e.com/api/2/btc_usd/ticker'))
	return data['ticker']['last']

def bitStamp():
	data = json_to_dict(get_URL('https://www.bitstamp.net/api/ticker/'))
	return data['last']

def campBX():
	#CampBx Gives a 403 Forbidden error if not supplying a user agent string,
	#forcing us to spoof one in the get_URL function.
	data = json_to_dict(get_URL('http://campbx.com/api/xticker.php'))
	return data['Last Trade']

def kraken():
	data = json_to_dict(get_URL('https://api.kraken.com/0/public/Ticker?pair=XBTUSD'))
	return data['result']['XXBTZUSD']['c'][0]

def crypto_trade():
	data = json_to_dict(get_URL('https://crypto-trade.com/api/1/ticker/btc_usd'))
	return data['data']['last']

def CoinMKT():
	# Their API endpoint is not yet public.
	return "Coming Soon."

def get_URL(url):
	#need to set a timeout
    try:
    	request = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"}) 
        result = urllib2.urlopen(request)
        return result.read()
    except urllib2.URLError, e:
           return "ERROR WITH URL: " + str(e) 

def json_to_dict(my_json):
    return json.loads(my_json)


#https://www.okcoin.com/api/ticker.do?symbol=ltc_cny    http://bter.com/api#ticker
#https://www.cryptsy.com/pages/api
# https://vircurex.com/welcome/api?locale=en
#http://api.virwox.com/api/documentation/Basic_API.pdf
#https://blockchain.info/api/exchange_rates_api
#https://cex.io/api/ticker/LTC/BTC 

##### EXAMPLE #######
print "Coindesk Bitcoin Price Index: " + coindeskBPI()
print "Bitfinex Last Price: " + bitfinex()
print "CoinBase Last Price: " + coinbase()
print "Mt.Gox Last Price: " + mtGox()
print "BTCE Last Price: " + str( btce() )
print "Crypto Trade Last Price: " + str( crypto_trade() )
print "BitStamp Last Price: " + bitStamp()
print "CampBX Last Price: " + campBX()
print "Kraken Last Price: " + kraken()
print "BTC China Last Price (Yuan): " + btcChina()
print "OK Coin Last Price (Yuan): " + btcChina()
print "CoinMKT Last Price: " + CoinMKT()
