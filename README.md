<div align="center">

# 📈 Real-Time Stock Risk Analytics Platform

### *Live market data. Instant risk signals. Zero lag.*

An end-to-end, event-driven pipeline that ingests **live stock prices**, computes **volatility-based risk metrics**, and surfaces it all in a slick **Power BI dashboard**.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![RabbitMQ](https://img.shields.io/badge/RabbitMQ-Event--Driven-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Finnhub](https://img.shields.io/badge/Finnhub-Live%20Market%20Data-00C176?style=for-the-badge)](https://finnhub.io/)

![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Made by](https://img.shields.io/badge/made%20by-Prateek%20Singh-purple?style=flat-square)

</div>

---

## ⚡ Why This Exists

Markets move in milliseconds — dashboards shouldn't lag behind. This platform streams live prices straight from **Finnhub**, pushes them through a **RabbitMQ** event pipeline, classifies risk on the fly, and lands everything in **MySQL** for **Power BI** to visualize in near real time.

> Think of it as a mini trading floor's risk desk — minus the shouting.

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[📡 Finnhub API] -->|Live Ticks| B[🐍 Producer]
    B -->|Publish| C[🐇 RabbitMQ]
    C -->|Consume| D[⚙️ Consumer]
    D -->|Risk Scoring| E[(🗄️ MySQL)]
    E -->|Live Query| F[📊 Power BI Dashboard]

    style A fill:#00C176,color:#fff
    style B fill:#3776AB,color:#fff
    style C fill:#FF6600,color:#fff
    style D fill:#3776AB,color:#fff
    style E fill:#4479A1,color:#fff
    style F fill:#F2C811,color:#000
```

**Flow:** `Finnhub API → Producer → RabbitMQ → Consumer → MySQL → Power BI`

---

## ✨ Features

| | Feature | Description |
|---|---------|-------------|
| 🔴 | **Real-Time Ingestion** | Streams live stock prices straight from the Finnhub API |
| 🔄 | **Event-Driven Design** | Decoupled producer/consumer architecture via RabbitMQ |
| 📉 | **Volatility-Based Risk Classification** | Flags stocks as Low / Medium / High risk based on live volatility |
| 🚀 | **Top Gainers & Losers** | Auto-ranks the biggest market movers in real time |
| 💓 | **Live Feed Health Monitoring** | Know instantly if the data pipeline drops a heartbeat |
| 📊 | **Interactive Power BI Dashboard** | Drill-down visuals for prices, risk bands, and trends |

---

## 🧰 Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Data Source** | Finnhub API |
| **Messaging** | RabbitMQ |
| **Processing** | Python (Producer / Consumer) |
| **Storage** | MySQL |
| **Visualization** | Power BI |

</div>

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- RabbitMQ Server
- MySQL Server
- Finnhub API key ([get one free here](https://finnhub.io/))
- Power BI Desktop

### Installation & Run

```bash
# 1️⃣ Clone the repo
git clone https://github.com/prateek02221/<your-repo-name>.git
cd <your-repo-name>

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Start RabbitMQ
sudo systemctl start rabbitmq-server

# 4️⃣ Run the producer (streams live prices → queue)
python producer.py

# 5️⃣ Run the consumer (processes → scores risk → stores in MySQL)
python consumer.py

# 6️⃣ Open Power BI, connect to MySQL, and hit Refresh 🔄
```

---

## 📊 Dashboard Preview


![Dashboard Preview](https://raw.githubusercontent.com/prateek02221/stock-risk-analytics/main/dashboards/Dashboard.png)
```
```

---

## 🗺️ Roadmap

- [ ] Add anomaly detection alerts (Slack/Telegram webhook)
- [ ] Historical volatility backtesting module
- [ ] Dockerize producer + consumer for one-command deploy
- [ ] Add sector-wise risk heatmap in Power BI

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](../../issues) or open a PR.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

## 👨‍💻 Author

**Prateek Singh**

[![GitHub](https://img.shields.io/badge/GitHub-prateek02221-181717?style=for-the-badge&logo=github)](https://github.com/prateek02221)

⭐ *If you found this project interesting, consider giving it a star!*

</div>
