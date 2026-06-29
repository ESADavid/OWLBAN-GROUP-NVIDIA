#!/usr/bin/env python3
"""Test CPU fallback implementations for RL and Quantum Monte Carlo"""

import sys
import os
import traceback
import numpy as np

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Top-level imports for optional dependencies
from performance_optimization.reinforcement_learning_agent import ReinforcementLearningAgent
from quantum_financial_ai.quantum_risk_analyzer import QuantumRiskAnalyzer, RiskFactor


def test_rl_agent():
    """Test RL agent with CPU fallback"""
    print("=" * 60)
    print("Testing Reinforcement Learning Agent (CPU Fallback)")
    print("=" * 60)

    try:
        # Create agent with use_gpu=False to force CPU
        agent = ReinforcementLearningAgent(
            actions=['increase', 'decrease', 'maintain', 'optimize'],
            learning_rate=0.001,
            discount_factor=0.99,
            epsilon=0.3,
            use_gpu=False
        )

        print(f"Device: {agent.device}")
        print(f"Action space: {agent.actions}")

        # Test simple episode
        state = [1.0, 2.0, 0.5, 0.3]

        for i in range(5):
            action = agent.choose_action(state)
            print(f"  Step {i+1}: Action = {action}")
            # Learn with simple feedback
            reward = 0.1 if action == 'optimize' else -0.05
            next_state = [1.5, 1.8, 0.6, 0.35]
            agent.learn(state, action, reward, next_state)
            state = next_state

        gpu_status = agent.get_gpu_status()
        print(f"GPU Status: {gpu_status}")

        print("\n✅ RL Agent CPU fallback test PASSED")
        return True

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"\n❌ RL Agent test FAILED: {e}")
        traceback.print_exc()
        return False


def test_quantum_risk():
    """Test Quantum Risk Analyzer with CPU fallback"""
    print("\n" + "=" * 60)
    print("Testing Quantum Risk Analyzer (CPU Fallback)")
    print("=" * 60)

    try:
        # Create analyzer with use_gpu=False to force CPU
        analyzer = QuantumRiskAnalyzer(confidence_level=0.95, use_gpu=False)

        print(f"Device: {analyzer.device}")

        # Add risk factors
        analyzer.add_risk_factor(RiskFactor(
            name="stockPortfolio",
            current_value=1000000,
            volatility=0.15
        ))
        analyzer.add_risk_factor(RiskFactor(
            name="bondPortfolio",
            current_value=500000,
            volatility=0.05
        ))
        analyzer.add_risk_factor(RiskFactor(
            name="commodities",
            current_value=300000,
            volatility=0.25
        ))

        # Test classical Monte Carlo
        portfolio_values = np.array([1000000, 500000, 300000])

        print("\nRunning Classical Monte Carlo (1000 simulations)...")
        result_classical = analyzer.analyze_risk(
            portfolio_values,
            method="classical",
            n_simulations=1000
        )
        print(f"  VaR: ${result_classical.value_at_risk:,.2f}")
        print(f"  CVaR: ${result_classical.conditional_var:,.2f}")

        print("\nRunning Quantum Monte Carlo (1000 simulations)...")
        result_quantum = analyzer.analyze_risk(
            portfolio_values,
            method="quantum",
            n_simulations=1000
        )
        print(f"  VaR: ${result_quantum.value_at_risk:,.2f}")
        print(f"  CVaR: ${result_quantum.conditional_var:,.2f}")
        print(f"  Quantum Advantage: {result_quantum.quantum_advantage}x")

        print("\n✅ Quantum Risk Analyzer CPU fallback test PASSED")
        return True

    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"\n❌ Quantum Risk Analyzer test FAILED: {e}")
        traceback.print_exc()
        return False


def main():
    """Main test function"""
    print("OWLBAN GROUP - CPU Fallback Implementations Test")
    print("=" * 60)

    results = []

    # Test RL Agent
    results.append(("RL Agent", test_rl_agent()))

    # Test Quantum Risk Analyzer
    results.append(("Quantum Risk Analyzer", test_quantum_risk()))

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    all_passed = True
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"  {name}: {status}")
        if not passed:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 All CPU fallback tests PASSED!")
        print("\nNote: Phase 3 operations can now run with CPU fallback.")
        print("For GPU acceleration, install PyTorch as per the installation guide.")
    else:
        print("\n⚠️ Some tests failed. Check errors above.")

    return all_passed


if __name__ == "__main__":
    SUCCESS = main()
    sys.exit(0 if SUCCESS else 1)
