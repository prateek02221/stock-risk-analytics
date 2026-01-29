# Real-Time Stock Risk Analytics Platform

An end-to-end real-time stock market analytics system that ingests live stock prices, calculates risk metrics, and visualizes insights using Power BI.

## Tech Stack
- Python
- RabbitMQ
- MySQL
- Power BI
- Finnhub API

## Features
- Real-time stock price ingestion
- Event-driven architecture with RabbitMQ
- Volatility-based risk classification
- Top gainers & losers analysis
- Live feed status monitoring
- Interactive Power BI dashboard

## Architecture
Finnhub API → Producer → RabbitMQ → Consumer → MySQL → Power BI

## How to Run
1. Start RabbitMQ
2. Run producer
3. Run consumer
4. Refresh Power BI dashboard

## Author
Prateek Singh
