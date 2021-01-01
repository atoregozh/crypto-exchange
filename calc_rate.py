from binance import calc_binance_withdrawals
from luno import calc_luno_withdrawals
import json


def exchange(from_amount, from_currency, to_currency):
    # Binance Converstion to Coin
    binance_withdrawal_list = calc_binance_withdrawals(from_amount)

    # Luno Converstion to destination currency
    luno_withdrawal_input = {}
    for binance_withdrawal in binance_withdrawal_list:
        currency_pair = '{}{}'.format(binance_withdrawal['to_symbol'], to_currency)
        input_dict = {
            'from_symbol': binance_withdrawal['to_symbol'],
            'from_name': binance_withdrawal['to_name'],
            'from_amount': binance_withdrawal['to_amount'],
            'to_symbol': to_currency,
        }
        luno_withdrawal_input.update({currency_pair: input_dict})

    luno_withdrawal_list = calc_luno_withdrawals(luno_withdrawal_input)

    # Format and sort result
    overall_exchange_result = []
    for luno_result in luno_withdrawal_list:
        overall_exchange_result.append({
            'from_currency': from_currency,
            'from_amount': from_amount,
            'coin_symbol': luno_result['from_symbol'],
            'coin_name': luno_result['from_name'],
            'coin_amount': luno_result['from_amount'],
            'coin_to_currency_fee': luno_result['trading_fee'],
            'to_currency': luno_result['to_symbol'],
            'to_amount': luno_result['to_amount'],
            'exchange_rate': luno_result['to_amount'] / from_amount
        })

    sorted_exchange_result = sorted(overall_exchange_result, key = lambda x: x['exchange_rate'], reverse=True)
    return sorted_exchange_result


if __name__ == '__main__':
    result_list = exchange(1000, 'USD', 'NGN')
    for single_exchange in result_list:
        print(json.dumps(single_exchange, indent=4, sort_keys=True))

