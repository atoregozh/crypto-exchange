-- append only exchange fees table
create table if not exists `crypto_exchange`.`exchange_fees`(
   `marketplace` VARCHAR(50) NOT NULL,
   `symbol` VARCHAR(10) NOT NULL,
   `fee_type` VARCHAR(20) NOT NULL,
   `amount` DECIMAL(19,4) NOT NULL,
   `amount_unit` VARCHAR(20) NOT NULL,
   `time_updated` BIGINT NOT NULL
);

-- append only exchange rates table for crypto/fiat or fiat/crypto pairs
create table if not exists `crypto_exchange`.`exchange_rates`(
   `marketplace` VARCHAR(50) NOT NULL,
   `from_symbol` VARCHAR(10) NOT NULL,
   `to_symbol` VARCHAR(10) NOT NULL,
   `rate` DECIMAL(19,4) NOT NULL,
   `time_updated` BIGINT NOT NULL
);

-- aggregate latest update crypto/fiat or fiat/crypto pairs exchange table
create table if not exists `crypto_exchange`.`exchange_aggregate`(
    `id` VARCHAR(80) NOT NULL,
    `marketplace` VARCHAR(50) NOT NULL,
    `from_symbol` VARCHAR(10) NOT NULL,
    `to_symbol` VARCHAR(10) NOT NULL,
    `rate` DECIMAL(19,4) NOT NULL,
    `trade_fee` DECIMAL(19,4) NULL,
    `deposit_fee` DECIMAL(19,4) NULL,
    `withdrawal_fee` DECIMAL(19,4) NULL,
    `time_updated` BIGINT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `marketplace_from_symbol_idx` (`marketplace`, `from_symbol`),
    INDEX `marketplace_to_symbol_idx` (`marketplace`, `to_symbol`)
);