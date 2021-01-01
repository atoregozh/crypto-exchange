from binance import calc_binance_withdrawals
from luno import calc_luno_withdrawals
import json

dollar_amt = 1000


def exchange(from_amount, from_currency, to_currency):
    binance_withdrawal_list = calc_binance_withdrawals(from_amount)
    luno_withdrawal_input = {
        '{}{}'.format(x['to_symbol'], to_currency) :
            {
                'from_symbol': x['to_symbol'],
                'from_name': x['to_name'],
                'from_amount': x['to_amount'],
                'to_symbol': to_currency,
            } for x in binance_withdrawal_list
        }

    luno_withdrawal_list = calc_luno_withdrawals(luno_withdrawal_input)

    exchange_result = [
        {
            'from_currency': from_currency,
            'from_amount': from_amount,
            'coin_symbol': luno_result['from_symbol'],
            'coin_name': luno_result['from_name'],
            'coin_amount': luno_result['from_amount'],
            'coin_to_currency_fee': luno_result['trading_fee'],
            'to_currency': luno_result['to_symbol'],
            'to_amount': luno_result['to_amount'],
            'exchange_rate': luno_result['to_amount'] / from_amount
        }
        for luno_result in luno_withdrawal_list
    ]

    return sorted(exchange_result, key = lambda x: x['exchange_rate'], reverse=True)


def calc_rate():
    result = exchange(dollar_amt, 'USD', 'NGN')
    for single_exchange in result:
        print(json.dumps(single_exchange, indent=4, sort_keys=True))


if __name__ == '__main__':
    calc_rate();


class ExchangeResult:
    def __init__(self, from_amount, from_currency, to_amount, to_currency, intermediate_coin, breakdown):
        self.from_amount = from_amount
        self.from_currency = from_currency
        self.to_amount = to_amount
        self.to_currency = to_currency
        self.intermediate_coin = intermediate_coin
        self.breakdown = breakdown


