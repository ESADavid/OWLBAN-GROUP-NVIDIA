#!/usr/bin/env python3
"""Quick revenue test script"""
import sys

class MockNIM:
    def get_resource_status(self):
        return {'GPU Usage': '50%', 'GPU Memory': '40GB'}
    def initialize(self):
        pass

try:
    from new_products.revenue_optimizer import NVIDIARevenueOptimizer
    
    nim = MockNIM()
    opt = NVIDIARevenueOptimizer(nim)
    
    profit = opt.get_current_profit()
    print(f'PROFIT: {profit}')
    
    # Quantum portfolio
    result = opt.optimize_quantum_portfolio()
    print(f'Sharpe: {result.sharpe_ratio}')
    
    # Risk
    risk = opt.analyze_quantum_risk()
    print(f'VaR: {risk.value_at_risk}')
    
    print('SUCCESS')
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)
