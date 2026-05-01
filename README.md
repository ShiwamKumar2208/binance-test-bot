# Binance Futures Testnet Trading Bot

A simple Python CLI-based trading bot for placing MARKET and LIMIT orders on Binance Futures Testnet.

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI input with validation
* Logging of requests and responses
* Clean structure (CLI + API logic separation)

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
API_KEY=your_key
API_SECRET=your_secret
```

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

## Notes

* Uses Binance Futures Testnet
* Logs are saved in `bot.log`
