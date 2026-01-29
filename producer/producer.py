import pika
import json
import time

from producer.fetch_stock_data import get_stock_price

symbols = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
    "META", "NVDA", "NFLX", "ORCL", "IBM",
    "INTC", "AMD", "ADBE", "CRM", "CSCO",
    "QCOM", "AVGO", "TXN", "PYPL", "UBER"
]

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.exchange_declare(
    exchange="stock_exchange",
    exchange_type="direct",
    durable=True
)

channel.queue_declare(
    queue="stock_events",
    durable=True
)

print("[*] Finnhub Producer started...")

while True:
    for symbol in symbols:
        stock_data = get_stock_price(symbol)

        if stock_data is None:
            print(f"[!] Skipped {symbol} (API limit / empty)")
            continue

        channel.basic_publish(
            exchange="stock_exchange",
            routing_key="stock.price",
            body=json.dumps(stock_data),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        print(f"[x] Sent {symbol} → {stock_data['price']}")

    time.sleep(30)
