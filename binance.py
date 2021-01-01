import requests
import json
from coin_exchange import CoinExchange

def get_binance_prices():
    r = requests.get('https://api.binance.us/api/v3/ticker/price')
    #print(json.dumps(r.json(), indent=2))
    binance_coin_prices = {}
    for symbol_price_dic in r.json():
        symbol = symbol_price_dic["symbol"]
        if symbol == "BTCUSD":
            binance_coin_prices["BTC"] = float(symbol_price_dic["price"])
        elif symbol == "ETHUSD":
            binance_coin_prices["ETH"] = float(symbol_price_dic["price"])
        elif symbol == "LTCUSD":
            binance_coin_prices["LTC"] = float(symbol_price_dic["price"])
        elif symbol == "XRPUSD":
            binance_coin_prices["XRP"] = float(symbol_price_dic["price"])
    return binance_coin_prices

def main():
    binance_coin_prices = get_binance_prices()
    print(binance_coin_prices)
    BTC_exchange = CoinExchange("BTC",
                                "Bitcoin",
                                "binance",
                                binance_coin_prices["BTC"],
                                0.1,
                                0.0005)
    ETH_exchange = CoinExchange("ETH",
                                "Etherium",
                                "binance",
                                binance_coin_prices["ETH"],
                                0.1,
                                0.013)
    XRP_exchange = CoinExchange("XRP",
                                "XRP",
                                "binance",
                                binance_coin_prices["XRP"],
                                0.1,
                                0.25)
    LTC_exchange = CoinExchange("LTC",
                                "Litecoin",
                                "binance",
                                binance_coin_prices["LTC"],
                                0.1,
                                0.001)

    fake_dollar_amount = 1000
    print(BTC_exchange.retrieve_coin_from_dollar(fake_dollar_amount))
    print(ETH_exchange.retrieve_coin_from_dollar(fake_dollar_amount))
    print(LTC_exchange.retrieve_coin_from_dollar(fake_dollar_amount))
    print(XRP_exchange.retrieve_coin_from_dollar(fake_dollar_amount))


def calc_binance_withdrawals(from_amount):
    binance_coin_prices = get_binance_prices()
    BTC_exchange = CoinExchange("BTC",
                                "Bitcoin",
                                "binance",
                                binance_coin_prices["BTC"],
                                0.1,
                                0.0005)
    ETH_exchange = CoinExchange("ETH",
                                "Ethereum",
                                "binance",
                                binance_coin_prices["ETH"],
                                0.1,
                                0.013)
    XRP_exchange = CoinExchange("XRP",
                                "XRP",
                                "binance",
                                binance_coin_prices["XRP"],
                                0.1,
                                0.25)
    LTC_exchange = CoinExchange("LTC",
                                "Litecoin",
                                "binance",
                                binance_coin_prices["LTC"],
                                0.1,
                                0.001)

    return [
        {
            'to_symbol': BTC_exchange.coin_symbol,
            'to_name': BTC_exchange.coin_name,
            'to_amount': BTC_exchange.retrieve_coin_from_dollar(from_amount)
        },
        {
            'to_symbol': ETH_exchange.coin_symbol,
            'to_name': ETH_exchange.coin_name,
            'to_amount': ETH_exchange.retrieve_coin_from_dollar(from_amount)
        },
        {
            'to_symbol': XRP_exchange.coin_symbol,
            'to_name': XRP_exchange.coin_name,
            'to_amount': XRP_exchange.retrieve_coin_from_dollar(from_amount)
        },
        {
            'to_symbol': LTC_exchange.coin_symbol,
            'to_name': LTC_exchange.coin_name,
            'to_amount': LTC_exchange.retrieve_coin_from_dollar(from_amount)
        },
    ]


if __name__ == "__main__":
    main()
