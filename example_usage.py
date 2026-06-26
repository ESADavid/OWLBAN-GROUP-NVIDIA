#!/usr/bin/env python3
"""
OWLBAN GROUP NVIDIA - Main Example Usage
=====================================
This is the main entry point demonstrating all key features of the OWLBAN GROUP 
Quantum AI Enterprise Platform.

Quick Start:
    python example_usage.py

For more details, see ONBOARDING.md
"""

import sys
import logging
import time
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("OWLBANExample")


def print_header(title: str) -> None:
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_success(message: str) -> None:
    """Print a success message"""
    print(f"✅ {message}")


def print_info(message: str) -> None:
    """Print an info message"""
    print(f"ℹ️  {message}")


def print_error(message: str) -> None:
    """Print an error message"""
    print(f"❌ {message}")


# =============================================================================
# SECTION 1: CORE AI SYSTEM
# =============================================================================

def demo_core_ai_system() -> bool:
    """Demonstrate the Core AI System"""
    print_header("1. Core AI System Demo")

    try:
        from combined_nim_owlban_ai import CombinedSystem, NimManager

        # Initialize NIM Manager
        print_info("Initializing NVIDIA NIM Manager...")
        nim = NimManager()
        nim.initialize()
        print_success("NIM Manager initialized")

        # Initialize Combined System
        print_info("Initializing Combined AI System...")
        ai = CombinedSystem()
        print_success("Combined System initialized")

        # Get system status
        gpu_status = nim.get_resource_status()
        print_info(f"GPU Status: {gpu_status}")

        print_success("Core AI System demo completed!")
        return True

    except ImportError as e:
        print_error(f"Import error: {e}")
        print_info("Install required packages: pip install -r combined_nim_owlban_ai/requirements.txt")
        return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False


def demo_ai_inference() -> bool:
    """Demonstrate AI Inference"""
    print_header("1b. AI Inference Demo")

    try:
        from combined_nim_owlban_ai import CombinedSystem

        # Initialize
        ai = CombinedSystem()

        # Sample input data
        input_data = {
            "feature1": 0.5,
            "feature2": 0.3,
            "feature3": 0.7,
            "feature4": 0.2,
            "feature5": 0.8
        }

        print_info(f"Input data: {input_data}")

        # Run inference
        result = ai.run_inference(input_data)
        print_info(f"Inference result: {result}")

        print_success("AI Inference demo completed!")
        return True

    except Exception as e:
        print_error(f"Error: {e}")
        return False


# =============================================================================
# SECTION 2: REVENUE OPTIMIZATION
# =============================================================================

def demo_revenue_optimizer() -> bool:
    """Demonstrate Revenue Optimization"""
    print_header("2. Revenue Optimizer Demo")

    try:
        from new_products.revenue_optimizer import NVIDIARevenueOptimizer
        from combined_nim_owlban_ai.nim import NimManager

        # Initialize
        print_info("Initializing Revenue Optimizer...")
        nim = NimManager()
        nim.initialize()
        optimizer = NVIDIARevenueOptimizer(nim)
        print_success("Revenue Optimizer initialized")

        # Run optimization
        print_info("Running revenue optimization (10 iterations)...")
        optimizer.optimize_revenue(iterations=10)

        # Get profit
        profit = optimizer.get_current_profit()
        print_info(f"Current Profit: ${profit:.2f}")

        print_success("Revenue Optimizer demo completed!")
        return True

    except ImportError as e:
        print_error(f"Import error: {e}")
        print_info("Revenue optimizer requires PyTorch - see ONBOARDING.md for alternatives")
        return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False


# =============================================================================
# SECTION 3: QUANTUM FINANCIAL AI
# =============================================================================

def demo_quantum_portfolio() -> bool:
    """Demonstrate Quantum Portfolio Optimization"""
    print_header("3. Quantum Portfolio Optimization Demo")

    try:
        from new_products.revenue_optimizer import NVIDIARevenueOptimizer
        from combined_nim_owlban_ai.nim import NimManager

        # Initialize
        nim = NimManager()
        nim.initialize()
        optimizer = NVIDIARevenueOptimizer(nim)

        # Optimize portfolio
        print_info("Optimizing quantum portfolio...")
        portfolio = optimizer.optimize_quantum_portfolio()

        print_info(f"Expected Return: {portfolio.expected_return:.4f}")
        print_info(f"Sharpe Ratio: {portfolio.sharpe_ratio:.4f}")
        print_info(f"Portfolio Volatility: {portfolio.portfolio_volatility:.4f}")

        # Risk analysis
        print_info("Analyzing quantum risk...")
        risk = optimizer.analyze_quantum_risk()

        print_info(f"Value at Risk (VaR): {risk.var:.4f}")
        print_info(f"Conditional VaR: {risk.cvar:.4f}")

        print_success("Quantum Portfolio demo completed!")
        return True

    except ImportError as e:
        print_error(f"Import error: {e}")
        return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False


def demo_quantum_market_prediction() -> bool:
    """Demonstrate Quantum Market Prediction"""
    print_header("3b. Quantum Market Prediction Demo")

    try:
        from new_products.revenue_optimizer import NVIDIARevenueOptimizer
        from combined_nim_owlban_ai.nim import NimManager

        # Initialize
        nim = NimManager()
        nim.initialize()
        optimizer = NVIDIARevenueOptimizer(nim)

        # Predict market
        print_info("Predicting market for TECH_STOCK...")
        prediction = optimizer.predict_market_with_quantum("TECH_STOCK")

        print_info(f"Direction: {prediction.direction}")
        print_info(f"Price Change: {prediction.price_change:.4f}")
        print_info(f"Confidence: {prediction.confidence:.4f}")

        print_success("Quantum Market Prediction demo completed!")
        return True

    except Exception as e:
        print_error(f"Error: {e}")
        return False


# =============================================================================
# SECTION 4: ANOMALY DETECTION
# =============================================================================

def demo_anomaly_detection() -> bool:
    """Demonstrate Anomaly Detection"""
    print_header("4. Anomaly Detection Demo")

    try:
        from new_products.anomaly_detection import AnomalyDetection
        from combined_nim_owlban_ai import NimManager, OwlbanAI

        # Initialize
        nim = NimManager()
        nim.initialize()
        ai = OwlbanAI()

        detector = AnomalyDetection(nim, ai)

        # Detect anomalies
        print_info("Detecting anomalies...")
        anomalies = detector.detect_anomalies()

        print_info(f"Detected {len(anomalies)} anomalies")

        print_success("Anomaly Detection demo completed!")
        return True

    except ImportError as e:
        print_error(f"Import error: {e}")
        return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False


# =============================================================================
# SECTION 5: INFRASTRUCTURE OPTIMIZER
# =============================================================================

def demo_infrastructure_optimizer() -> bool:
    """Demonstrate Infrastructure Optimization"""
    print_header("5. Infrastructure Optimizer Demo")

    try:
        from new_products.infrastructure_optimizer import InfrastructureOptimizer
        from combined_nim_owlban_ai.nim import NimManager

        # Initialize
        nim = NimManager()
        nim.initialize()
        optimizer = InfrastructureOptimizer(nim)

        # Optimize resources
        print_info("Optimizing infrastructure resources...")
        optimizer.optimize_resources()

        print_success("Infrastructure Optimizer demo completed!")
        return True

    except ImportError as e:
        print_error(f"Import error: {e}")
        return False

    except Exception as e:
        print_error(f"Error: {e}")
        return False


# =============================================================================
# SECTION 6: DATABASE OPERATIONS
# =============================================================================

def demo_database_operations() -> bool:
    """Demonstrate Database Operations"""
    print_header("6. Database Operations Demo")

    try:
        from database_manager import DatabaseManager

        # Initialize
        db = DatabaseManager()

        # Get status
        status = db.get_database_status()
        print_info(f"Database Status: {status}")

# Save a prediction
        print_info("Saving sample prediction...")
        db.save_prediction(
            model_name="example_model",
            input_data={"feature1": 0.5},
            prediction={"prediction": 0.8},
            confidence=0.85
        )

        # Get recent predictions
        predictions = db.get_predictions(limit=5)
        print_info(f"Retrieved {len(predictions)} predictions")

        print_success("Database Operations demo completed!")
        return True

    except Exception as e:
        print_error(f"Error: {e}")
        return False


# =============================================================================
# SECTION 7: API SERVER (Mock)
# =============================================================================

def demo_api_server() -> None:
    """Demonstrate API Server endpoints"""
    print_header("7. API Server Demo (Reference)")

    print_info("API Server can be started with:")
    print("  python api_server.py")
    print()
    print_info("Available endpoints:")
    print("  GET  /              - Root endpoint")
    print("  GET  /health        - Health check")
    print("  GET  /status        - System status")
    print("  GET  /gpu/status     - GPU status")
    print("  POST /revenue/optimize - Run revenue optimization")
    print("  GET  /revenue/profit - Get current profit")
    print("  GET  /quantum/portfolio - Quantum portfolio")
    print("  GET  /quantum/risk    - Quantum risk analysis")
    print()
    print_info("Example curl commands:")
    print("  curl http://localhost:8000/health")
    print("  curl http://localhost:8000/status")


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def run_all_demos() -> Dict[str, bool]:
    """Run all demonstration functions"""
    results = {}

    print("\n" + "#" * 60)
    print("#  OWLBAN GROUP NVIDIA - Main Example Usage")
    print("#" * 60)
    print(f"#  Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("#" * 60)

    # Run demos
    demos = [
        ("Core AI System", demo_core_ai_system),
        ("AI Inference", demo_ai_inference),
        ("Revenue Optimizer", demo_revenue_optimizer),
        ("Quantum Portfolio", demo_quantum_portfolio),
        ("Quantum Market Prediction", demo_quantum_market_prediction),
        ("Anomaly Detection", demo_anomaly_detection),
        ("Infrastructure Optimizer", demo_infrastructure_optimizer),
        ("Database Operations", demo_database_operations),
    ]

    for name, demo_func in demos:
        try:
            results[name] = demo_func()
        except Exception as e:
            logger.error(f"Demo {name} failed: {e}")
            results[name] = False

    # Show API server info
    demo_api_server()

    # Summary
    print_header("Summary")

    successful = sum(1 for v in results.values() if v)
    total = len(results)

    for name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {name}: {status}")

    print(f"\nTotal: {successful}/{total} demos passed")

    if successful == total:
        print_success("All demos completed successfully!")
    else:
        print_info("Some demos failed - see ONBOARDING.md for troubleshooting")

    print(f"\nCompleted at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    return results


def main():
    """Main entry point"""
    try:
        results = run_all_demos()

        # Exit with error if all demos failed
        if not any(results.values()):
            print_error("All demos failed - check dependencies and ONBOARDING.md")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
        sys.exit(0)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
