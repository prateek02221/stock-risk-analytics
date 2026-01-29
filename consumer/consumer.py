import pika
import json

from consumer.risk_calculator import calculate_risk
from database.db_insert import insert_stock_data


def callback(ch, method, properties, body):
    data = json.loads(body)

    print("[CONSUMER RECEIVED]:", data.get("symbol"))

    risk = calculate_risk(data)
    insert_stock_data(data, risk)


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

channel.queue_bind(
    exchange="stock_exchange",
    queue="stock_events",
    routing_key="stock.price"
)

print("[*] Consumer waiting for messages...")
channel.basic_consume(
    queue="stock_events",
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()
