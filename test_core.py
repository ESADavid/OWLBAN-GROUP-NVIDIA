#!/usr/bin/env python3
"""Test quantum components only (no PyTorch)"""
import sys
import logging
logging.basicConfig(level=logging.ERROR)

try:
    from database_manager import DatabaseManager
    db = DatabaseManager()
    status = db.get_database_status()
    print(f"DATABASE: {status}")
except Exception as e:
    print(f"DB ERROR: {e}")

try:
    from quantum_financial_ai.quantum_portfolio_optimizer import QuantumPortfolioOptimizer
    opt = QuantumPortfolioOptimizer(use_gpu=False)
    opt.add_asset(type('Asset', (), {'symbol': 'TEST', 'expected_return': 0.1, 'volatility': 0.2, 'current_price': 100, 'quantity': 10})())
    result = opt.optimize_portfolio(method="classical")
    print(f"PORTFOLIO: Sharpe={result.sharpe_ratio}")
except Exception as e:
    print(f"PORTFOLIO ERROR: {e}")

try:
    from quantum_financial_ai.quantum_risk_analyzer import QuantumRiskAnalyzer, RiskFactor
    ana = QuantumRiskAnalyzer(use_gpu=False)
    ana.add_risk_factor(RiskFactor("Market_Volatility", 0.15, 0.20))
    import numpy as np
    res = ana.analyze_risk(np.array([1000]), method="classical")
    print(f"RISK: VaR={res.value_at_risk:.4f}")
except Exception as e:
    print(f"RISK ERROR: {e}")

print("CORE TEST COMPLETE")
