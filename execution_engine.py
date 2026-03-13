import alpaca_trade_api as tradeapi
from config_loader import load_config

config = load_config()

api = tradeapi.REST(
    config["API_KEY"],
    config["API_SECRET"],
    config["BASE_URL"]
)

def rebalance(weights):

    account = api.get_account()

    equity = float(account.equity)

    for ticker,weight in weights.items():

        target_value = equity * weight

        price = api.get_latest_trade(ticker).price

        qty = int(target_value / price)

        api.submit_order(
            symbol=ticker,
            qty=qty,
            side="buy",
            type="market",
            time_in_force="day"
        )
