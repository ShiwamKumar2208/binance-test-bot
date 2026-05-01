from binance.client import Client
import os
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logging.info(f"REQUEST: {params}")

        res = client.futures_create_order(**params)

        logging.info(f"RESPONSE: {res}")

        return res

    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}