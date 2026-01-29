import mysql.connector

# Create DB connection ONCE
conn = mysql.connector.connect(
    host="localhost",
    user="stock_user",
    password="StrongPassword@123",  # use your actual password
    database="stock_analytics"
)

# Create cursor ONCE
cursor = conn.cursor()


def insert_stock_data(data, risk):
    query = """
    INSERT INTO stock_prices (symbol, price, volatility, risk_level)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        data["symbol"],
        data["price"],
        risk["volatility"],
        risk["risk_level"]
    )

    cursor.execute(query, values)
    conn.commit()
