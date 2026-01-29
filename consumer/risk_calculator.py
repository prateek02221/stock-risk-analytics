def calculate_risk(data):
    price = data.get("price", 0)

    if price == 0:
        return {
            "volatility": 0.0,
            "risk_level": "UNKNOWN"
        }

    # simple volatility proxy
    volatility = price * 0.015

    return {
        "volatility": volatility,
        "risk_level": "HIGH" if volatility > 5 else "LOW"
    }
