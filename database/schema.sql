CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10),
    price FLOAT,
    volatility FLOAT,
    risk_level VARCHAR(10),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
