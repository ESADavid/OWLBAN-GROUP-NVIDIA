# OWLBAN GROUP NVIDIA - Quantum AI Enterprise Platform

[![CI](https://github.com/OWLBAN-GROUP-NVIDIA/actions/workflows/ci.yml/badge.svg)](https://github.com/OWLBAN-GROUP-NVIDIA/actions)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Enterprise-green.svg)](LICENSE)

Welcome to the **OWLBAN GROUP Quantum AI Enterprise Platform** - a comprehensive quantum-accelerated AI system integrating NVIDIA NIM, OWLBAN AI, and enterprise-grade financial applications.

## Quick Start

Get up and running in 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/OWLBAN-GROUP-NVIDIA.git
cd OWLBAN-GROUP-NVIDIA

# 2. Install dependencies
pip install -r combined_nim_owlban_ai/requirements.txt
pip install fastapi uvicorn streamlit pandas plotly requests numpy

# 3. Run the example
python example_usage.py
```

## Features

- **Quantum AI System**: NVIDIA NIM + OWLBAN AI integration with quantum acceleration
- **Revenue Optimization**: AI-powered revenue maximization with reinforcement learning
- **Quantum Portfolio Optimization**: Quantum-enhanced portfolio management
- **Anomaly Detection**: AI-powered security threat detection
- **API Server**: FastAPI-based REST API with full CRUD operations
- **Web Dashboard**: Streamlit-based monitoring dashboard

## Documentation

- [ONBOARDING.md](ONBOARDING.md) - Complete onboarding guide
- [PROJECT_MASTER_PLAN.md](PROJECT_MASTER_PLAN.md) - Strategic roadmap
- [COMPLETE_MASTER_PLAN.md](COMPLETE_MASTER_PLAN.md) - Full enterprise plan

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|------------|
| Python | 3.11+ | 3.11+ |
| RAM | 8GB | 16GB+ |
| Disk | 10GB | 50GB+ |
| OS | Windows 10+, macOS, Linux | Ubuntu 22.04+ |

## Installation

### Option 1: Install All Dependencies

```bash
# Core dependencies
pip install -r combined_nim_owlban_ai/requirements.txt

# Additional dependencies for full functionality
pip install fastapi uvicorn streamlit pandas plotly requests numpy
```

### Option 2: Using Docker

```bash
# Build API server image
docker build -f Dockerfile.api -t owlban-api .

# Run the container
docker run -p 8000:8000 owlban-api
```

## Usage Examples

### Run Main Example

```bash
python example_usage.py
```

### Start API Server

```bash
python api_server.py
# Or with custom port
python -m uvicorn api_server:fastapi_app --host 0.0.0.0 --port 8000
```

### Start Web Dashboard

```bash
streamlit run web_dashboard.py
```

### Run Tests

```bash
# Run pytest
pytest tests/ -v

# Run E2E smoke test
python tests/test_e2e_smoke.py
```

## Project Structure

```
OWLBAN-GROUP-NVIDIA/
├── combined_nim_owlban_ai/     # Core AI Framework
│   ├── __init__.py             # Main exports
│   ├── nim.py                  # NVIDIA NIM Manager
│   ├── owlban_ai.py            # OWLBAN AI System
│   └── config/                 # Configuration
├── new_products/               # Product Modules
│   ├── revenue_optimizer.py    # Revenue optimization
│   ├── anomaly_detection.py   # Anomaly detection
│   └── infrastructure_optimizer.py
├── quantum_financial_ai/      # Quantum Financial AI
│   ├── quantum_portfolio_optimizer.py
│   ├── quantum_risk_analyzer.py
│   └── quantum_machine_learning_pipeline.py
├── api_server.py              # REST API Server
├── web_dashboard.py           # Streamlit Dashboard
├── example_usage.py           # Main entry point
├── ONBOARDING.md              # Onboarding guide
└── tests/                     # Test Suite
```

## API Endpoints

Once the API server is running:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/status` | System status |
| GET | `/gpu/status` | GPU status |
| POST | `/revenue/optimize` | Run revenue optimization |
| GET | `/revenue/profit` | Get current profit |
| GET | `/quantum/portfolio` | Quantum portfolio |
| GET | `/quantum/risk` | Quantum risk analysis |
| POST | `/inference` | Run AI inference |

## Technology Stack

- **AI Framework**: NVIDIA NIM, OWLBAN AI, PyTorch
- **Quantum Computing**: Qiskit, Quantum ML
- **API Framework**: FastAPI, Uvicorn
- **Web Dashboard**: Streamlit, Plotly
- **Database**: SQLite (default), PostgreSQL support
- **Monitoring**: DCGM, Prometheus, Grafana

## Getting Help

- **Onboarding Guide**: See [ONBOARDING.md](ONBOARDING.md)
- **Project Plans**: See [PROJECT_MASTER_PLAN.md](PROJECT_MASTER_PLAN.md)
- **Issue Tracker**: Report issues on GitHub

## License

Enterprise License - All Rights Reserved

---

**OWLBAN GROUP** - Building the Future of Quantum AI
