import yfinance as yf
import pandas as pd

def predict_returns(tickers):

    predictions = {}

    for t in tickers:

        data = yf.download(t, period="1mo")

        ret = data["Close"].pct_change().mean()

        predictions[t] = ret

    return predictions
