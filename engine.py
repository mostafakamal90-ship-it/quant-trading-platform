from universe_builder import build_universe
from ai_models import predict_returns
from portfolio_optimizer import optimize_portfolio
from execution_engine import rebalance
from regime_detector import detect_regime
from risk_manager import apply_risk_controls

def run_cycle():

    print("Running trading cycle")

    universe = build_universe()

    predictions = predict_returns(universe)

    regime = detect_regime()

    weights = optimize_portfolio(predictions, regime)

    weights = apply_risk_controls(weights)

    rebalance(weights)
