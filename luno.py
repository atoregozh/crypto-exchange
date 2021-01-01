from luno_python.client import Client
import configparser
import datetime
import time

luno_withdrawal_fee_ngn = 200

binance_to_luno_symbol = {
    'BTC': 'XBT',
}


def get_luno_client():
    config = configparser.RawConfigParser()
    config.read('secret.properties')

    luno_key_id = config.get('LunoSection', 'luno.key_id')
    luno_secret = config.get('LunoSection', 'luno.secret')
    return Client(api_key_id=luno_key_id, api_key_secret=luno_secret)


def calc_luno_withdrawals(request_map):
    """
        :param request_map: A dict which maps strings to dict objects of format { currency_pair: { from_symbol: string, 'from_name': string, 'from_amount': int, 'to_symbol': string } }
        :return: list of dict objects with keys: from_symbol, from_name, from_amount, to_symbol, to_amount
        """

    luno_to_binance_currency_pairs = {
        '{}{}'.format(
            binance_to_luno_symbol.get(val['from_symbol'], val['from_symbol']),
            binance_to_luno_symbol.get(val['to_symbol'], val['to_symbol']))
        : key
        for key, val in request_map.items()
    }

    luno_client = get_luno_client()
    luno_tickers = luno_client.get_tickers()
    results = []
    for ticker in luno_tickers['tickers']:
        luno_currency_pair = ticker['pair']
        if luno_currency_pair not in luno_to_binance_currency_pairs:
            continue

        time.sleep(0.5)  # To account for trading fee API Rate limit
        fee_response = luno_client.get_fee_info(luno_currency_pair)
        trading_fee = max(float(fee_response['maker_fee']), float(fee_response['taker_fee']))

        request_currency_pair = luno_to_binance_currency_pairs[luno_currency_pair]
        request_object = request_map[request_currency_pair]

        from_amount = request_object['from_amount']
        from_amount_minus_trading_fee = from_amount - (from_amount * trading_fee)

        to_amount = from_amount_minus_trading_fee * float(ticker['last_trade'])

        to_amount_minus_withdrawal_fee = to_amount - luno_withdrawal_fee_ngn

        results.append({
            'from_symbol': request_object['from_symbol'],
            'from_name': request_object['from_name'],
            'from_amount': request_object['from_amount'],
            'to_symbol': request_object['to_symbol'],
            'to_amount': to_amount_minus_withdrawal_fee,
            'trading_fee': trading_fee,
            'withdrawal_fee': luno_withdrawal_fee_ngn,
        })

    return results


def run_luno():
    luno_client = get_luno_client()
    try:
        res = luno_client.get_ticker(pair='XBTZAR')
        print(res)
        print(datetime.datetime.utcfromtimestamp(res['timestamp'] / 1000))

        time.sleep(0.5)
        res = luno_client.get_fee_info('XBTNGN')
        print(res)

        time.sleep(0.5)
        res = luno_client.get_tickers()
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run_luno()