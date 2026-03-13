MAX_POSITION = 0.15

def apply_risk_controls(weights):

    adjusted = {}

    for ticker,w in weights.items():

        adjusted[ticker] = min(w,MAX_POSITION)

    return adjusted
