from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL
from logger import get_logger

class BasicBot:
    def __init__(self):
        self.logger = get_logger()
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL
        self.logger.info("Bot initialized")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_data = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                if price is None:
                    raise ValueError("Limit orders require a price.")
                order_data["price"] = price
                order_data["timeInForce"] = "GTC"

            order = self.client.futures_create_order(**order_data)
            self.logger.info(f"{side} {order_type} order placed: {order}")
            return order

        except Exception as e:
            self.logger.error(f"Order failed: {str(e)}")
            return {"error": str(e)}