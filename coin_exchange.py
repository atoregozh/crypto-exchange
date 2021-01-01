class CoinExchange:
    """
    Represents dollar to coin exchange - start with dollar, end with coin after all fees
    """
    def __init__(self, coin_symbol, coin_name, marketplace, exchange_rate, trading_fee_percent, withdrawal_fee):
        self.coin_symbol = coin_symbol  # e.g. BTC
        self.coin_name = coin_name # e.g. bitcoin
        self.marketplace = marketplace  # e.g. binance
        self.exchange_rate = exchange_rate # $/1 coin
        self.trading_fee_percent = trading_fee_percent # e.g. 0.1% per trade amount
        self.withdrawal_fee = withdrawal_fee # coin withdrawal fee

    def retrieve_coin_from_dollar(self, dollar_amount):
        trading_fee = dollar_amount * self.trading_fee_percent / 100
        purchased_coin = (dollar_amount - trading_fee) / self.exchange_rate
        retrieved_coin = purchased_coin - self.withdrawal_fee
        return retrieved_coin
