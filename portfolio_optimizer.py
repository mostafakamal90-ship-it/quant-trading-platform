def optimize_portfolio(predictions, regime):

    sorted_assets = sorted(
        predictions,
        key=predictions.get,
        reverse=True
    )

    top = sorted_assets[:5]

    weight = 1/len(top)

    weights = {t:weight for t in top}

    return weights
