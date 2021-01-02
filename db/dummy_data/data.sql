-- hardcoded values for exchange fees
INSERT INTO `crypto_exchange`.`exchange_fees`
(`marketplace`, `symbol`, `fee_type`, `amount`, `amount_unit`, `time_updated`)
VALUES
('binance.us', 'BTC', 'trade', 0.1, 'percent', 1609561433),
('binance.us', 'ETH', 'trade', 0.1, 'percent', 1609561433),
('binance.us', 'LTC', 'trade', 0.1, 'percent', 1609561433),
('binance.us', 'XRP', 'trade', 0.1, 'percent', 1609561433),
('binance.us', 'BTC', 'withdrawal', 0.0005, 'BTC', 1609561433),
('binance.us', 'ETH', 'withdrawal', 0.013, 'ETH', 1609561433),
('binance.us', 'LTC', 'withdrawal', 0.001, 'LTC', 1609561433),
('binance.us', 'XRP', 'withdrawal', 0.25, 'XRP', 1609561433),
('binance.us', 'USD', 'deposit', 0, 'USD', 1609561433),
('luno', 'BTC', 'deposit', 0, 'BTC', 1609561433),
('luno', 'ETH', 'deposit', 0, 'ETH', 1609561433),
('luno', 'LTC', 'deposit', 0, 'LTC', 1609561433),
('luno', 'XRP', 'deposit', 0, 'XRP', 1609561433),
('luno', 'NGN', 'withdrawal', 200, 'NGN', 1609561433),
('luno', 'BTC', 'trade', 0.1, 'percent', 1609561433),
('luno', 'ETH', 'trade', 0.1, 'percent', 1609561433),
('luno', 'LTC', 'trade', 0.1, 'percent', 1609561433),
('luno', 'XRP', 'trade', 0.1, 'percent', 1609561433)
;
