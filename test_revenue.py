#!/usr/bin/env python3
"""Test revenue operations"""
import sys
import logging

# Suppress warnings
logging.basicConfig(level=logging.ERROR)

class MockNIM:
    def get_resource_status(self):
        return {'GPU Usage': '50%', 'GPU Memory': '40GB'}
    def initialize(self):
        pass

try:
    from new_products.revenue_optimizer import NVIDIARevenueOptimizer
    from database_manager import DatabaseManager
    
    # Test database
    db = DatabaseManager()
    db_status = db.get_database_status()
    with open('test_output.txt', 'w') as f:
        f.write(f"DB Status: {db_status}\n")
    
    # Test revenue optimizer
    nim = MockNIM()
    opt = NVIDIARevenueOptimizer(nim)
    
    profit = opt.get_current_profit()
    with open('test_output.txt', 'a') as f:
        f.write(f"Profit: {profit}\n")
    
    # Quantum portfolio
    result = opt.optimize_quantum_portfolio()
    with open('test_output.txt', 'a') as f:
        f.write(f"Sharpe: {result.sharpe_ratio}\n")
    
    # Risk analysis
    risk = opt.analyze_quantum_risk()
    with open('test_output.txt', 'a') as f:
        f.write(f"VaR: {risk.value_at_risk}\n")
        f.write("SUCCESS\n")
    
    print("DONE - Check test_output.txt")
except Exception as e:
    with open('test_output.txt', 'w') as f:
        f.write(f"ERROR: {e}\n")
    print(f"ERROR: {e}")
