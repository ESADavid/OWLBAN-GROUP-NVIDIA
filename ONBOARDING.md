# OWLBAN GROUP NVIDIA - Onboarding Guide

Welcome to OWLBAN GROUP's Quantum AI Enterprise Platform! This guide will help you get started with the system in under 30 minutes.

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Quick Start](#2-quick-start)
3. [Project Structure](#3-project-structure)
4. [Basic Usage](#4-basic-usage)
5. [API Examples](#5-api-examples)
6. [Running Tests](#6-running-tests)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Prerequisites

### System Requirements

- **Python**: 3.11 or higher
- **Operating System**: Windows 10+, macOS, or Linux
- **Memory**: 8GB RAM minimum (16GB recommended)
- **Storage**: 10GB free space

### Required Dependencies

Install the required Python packages:

```bash
pip install -r combined_nim_owlban_ai/requirements.txt
```

Additional dependencies for full functionality:

```bash
pip install fastapi uvicorn streamlit pandas plotly requests numpy
```

---

## 2. Quick Start

### Option A: Run the Pre-built Example

```bash
# Run the main example demonstrating all features
python new_products/example_usage.py
```

### Option B: Start the API Server

```bash
# Start the API server (default port 8000)
python api_server.py

# Or run in background
python -m uvicorn api_server:fastapi_app --host 0.0.0.0 --port 8000
```

### Option C: Start the Web Dashboard

```bash
# Start the Streamlit dashboard
streamlit run web_dashboard.py
```

---

## 3. Project Structure

```
OWLBAN-GROUP-NVIDIA/
├── combined_nim_owlban_ai/     # Core AI Framework
│   ├── __init__.py             # Main exports
│   ├── nim.py                  # NVIDIA NIM Manager
│   ├── owlban_ai.py            # OWLBAN AI System
│   ├── quantum_financial_omniscient_system.py
│   ├── multi_modal_ai.py
│   └── config/                 # Configuration files
├── new_products/               # Product Modules
│   ├── revenue_optimizer.py    # Revenue optimization
│   ├── infrastructure_optimizer.py
│   ├── anomaly_detection.py
│   └── telehealth_analytics.py
├── quantum_financial_ai/      # Quantum Financial AI
│   ├── quantum_market_predictor.py
│   ├── quantum_portfolio_optimizer.py
│   ├── quantum_risk_analyzer.py
│   └── quantum_machine_learning_pipeline.py
├── api_server.py              # REST API Server
├── web_dashboard.py            # Web Dashboard (Streamlit)
├── tests/                     # Test Suite
└── .github/workflows/          # CI/CD Pipeline
```

---

## 4. Basic Usage

### 4.1 Initialize the AI System

```python
from combined_nim_owlban_ai import CombinedSystem, NimManager

# Initialize NVIDIA NIM Manager
nim = NimManager()
nim.initialize()

# Initialize the Combined AI System
ai = CombinedSystem()
print("✅ System initialized successfully!")
```

### 4.2 Run AI Inference

```python
from combined_nim_owlban_ai import CombinedSystem

ai = CombinedSystem()

# Run inference with sample data
input_data = {
    "feature1": 0.5,
    "feature2": 0.3,
    "feature3": 0.7
}

result = ai.run_inference(input_data)
print(f"Inference result: {result}")
```

### 4.3 Revenue Optimization

```python
from new_products.revenue_optimizer import NVIDIARevenueOptimizer
from combined_nim_owlban_ai.nim import NimManager

# Initialize
nim = NimManager()
nim.initialize()
optimizer = NVIDIARevenueOptimizer(nim)

# Run optimization
optimizer.optimize_revenue(iterations=10)

# Get current profit
profit = optimizer.get_current_profit()
print(f"Current Profit: ${profit:.2f}")
```

### 4.4 Quantum Portfolio Optimization

```python
from new_products.revenue_optimizer import NVIDIARevenueOptimizer
from combined_nim_owlban_ai.nim import NimManager

nim = NimManager()
nim.initialize()
optimizer = NVIDIARevenueOptimizer(nim)

# Optimize quantum portfolio
portfolio = optimizer.optimize_quantum_portfolio()
print(f"Expected Return: {portfolio.expected_return:.4f}")
print(f"Sharpe Ratio: {portfolio.sharpe_ratio:.4f}")
```

### 4.5 Anomaly Detection

```python
from new_products.anomaly_detection import AnomalyDetection
from combined_nim_owlban_ai import NimManager, OwlbanAI

nim = NimManager()
nim.initialize()
ai = OwlbanAI()

detector = AnomalyDetection(nim, ai)
anomalies = detector.detect_anomalies()

print(f"Detected {len(anomalies)} anomalies")
```

---

## 5. API Examples

### 5.1 REST API Endpoints

Once the API server is running (`python api_server.py`), you can access these endpoints:

```bash
# Health check
curl http://localhost:8000/health

# System status
curl http://localhost:8000/status

# Get GPU status
curl http://localhost:8000/gpu/status

# Revenue optimization
curl -X POST http://localhost:8000/revenue/optimize \
  -H "Content-Type: application/json" \
  -d '{"iterations": 10}'

# Get current profit
curl http://localhost:8000/revenue/profit

# Quantum portfolio optimization
curl http://localhost:8000/quantum/portfolio

# Quantum risk analysis
curl http://localhost:8000/quantum/risk
```

### 5.2 Python API Client

```python
import requests

API_BASE = "http://localhost:8000"

# Get system status
response = requests.get(f"{API_BASE}/status")
print(response.json())

# Run inference
response = requests.post(f"{API_BASE}/inference", json={
    "data": {"feature1": 0.5, "feature2": 0.3},
    "model_type": "prediction"
})
print(response.json())
```

---

## 6. Running Tests

### 6.1 Run All Tests

```bash
# Using pytest
pytest tests/ -v

# Or using the E2E smoke test
python tests/test_e2e_smoke.py
```

### 6.2 Run E2E Registration Test

```bash
# Run the NVIDIA partner registration E2E test
python nvidia_partner_registration_e2e.py
```

### 6.3 Run Example Usage

```bash
# Run all examples
python new_products/example_usage.py

# Run quantum ML examples
python quantum_financial_ai/example_usage_quantum_ml.py
```

---

## 7. Troubleshooting

### Issue: PyTorch Installation Failed

**Solution**: If you encounter Windows DLL issues, try:

```bash
# Option 1: Use CPU-only PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Option 2: Use Docker
docker build -f Dockerfile.api -t owlban-api .
```

### Issue: Database Connection Failed

**Solution**: The system uses SQLite by default. Check:

```python
from database_manager import DatabaseManager
db = DatabaseManager()
print(db.get_database_status())
```

### Issue: API Server Not Starting

**Solution**: Check port availability:

```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Use a different port
python -m uvicorn api_server:fastapi_app --port 8001
```

### Issue: Missing Dependencies

**Solution**: Install all required packages:

```bash
pip install -r combined_nim_owlban_ai/requirements.txt
pip install pandas numpy plotly requests
```

---

## Next Steps

1. **Explore the Code**: Review `new_products/example_usage.py` for detailed examples
2. **Start the Dashboard**: Run `streamlit run web_dashboard.py` for visual interface
3. **Run Tests**: Execute `python tests/test_e2e_smoke.py` to verify setup
4. **Review Documentation**: Check `README.md` and `PROJECT_MASTER_PLAN.md`

---

## Getting Help

- **Documentation**: See `README.md` for full project details
- **Master Plan**: See `PROJECT_MASTER_PLAN.md` for strategic roadmap
- **Issues**: Check the console output for error messages

---

## System Status

After setup, verify your installation:

```python
from combined_nim_owlban_ai import CombinedSystem, NimManager
from database_manager import DatabaseManager

# Check all components
nim = NimManager()
nim.initialize()
ai = CombinedSystem()
db = DatabaseManager()

print("✅ All systems initialized!")
print(f"GPU Status: {nim.get_resource_status()}")
print(f"Database: {db.get_database_status()}")
```

---

Happy coding! 🚀
