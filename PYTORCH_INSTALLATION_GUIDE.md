# PyTorch Installation Guide for OWLBAN GROUP NVIDIA AI

This guide provides instructions for installing PyTorch for GPU-accelerated operations on Linux, WSL, and Docker environments.

---

## Current Status

| Component | CPU Fallback | GPU Accelerated |
| ----- | ----- | ----- |
| RL Agent | ✅ Working | 🔲 Requires PyTorch |
| Quantum Risk Analyzer | ✅ Working | 🔲 Requires PyTorch |
| Anomaly Detection | 🔲 TBD | 🔲 Requires PyTorch |

**Note:** Phase 3 operations now work with CPU fallback. Install PyTorch for GPU acceleration.

---

## Installation Options

### Option 1: Windows (Direct Installation)

```powershell
# Install PyTorch with CPU only (quick test)
pip install torch torchvision torchaudio

# For NVIDIA GPU support (requires CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### Option 2: Windows Subsystem for Linux (WSL)

```bash
# Install Ubuntu/WSL first, then:

# Update package list
sudo apt update && sudo apt install -y python3-pip

# Install PyTorch with CUDA support
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Verify installation
python3 -c "import torch; print(f'PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}')"
```

### Option 3: Docker Installation

Create a Dockerfile for GPU-accelerated PyTorch:

```dockerfile
# Use NVIDIA CUDA base image
FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

# Set environment
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch with CUDA
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Default command
CMD ["python3", "-c", "import torch; print(f'PyTorch {torch.__version__}, CUDA: {torch.cuda.is_available()}')"]
```

Build and run:

```bash
# Build the image
docker build -t owlban-pytorch .

# Run with GPU support (requires nvidia-docker)
docker run --gpus all -it owlban-pytorch
```

---

## NVIDIA GPU Setup (Linux/WSL/Docker)

### Prerequisites

1. **NVIDIA Driver**: Install NVIDIA driver version 525.x or later
2. **CUDA Toolkit**: Version 12.1 or later
3. **cuDNN**: Version 8.9 or later

### Installation Steps

```bash
# 1. Add NVIDIA repository
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"

# 2. Install NVIDIA packages
sudo apt update
sudo apt install nvidia-utils-525 cuda-toolkit-12-1

# 3. Install cuDNN
sudo apt install libcudnn8

# 4. Install nvidia-docker (for Docker)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt update
sudo apt install -y nvidia-docker2
sudo systemctl restart docker

# 5. Verify
nvidia-smi
```

---

## Verify Installation

### Basic Verification

```python
import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
```

### Test RL Agent with GPU

```python
from performance_optimization.reinforcement_learning_agent import ReinforcementLearningAgent

agent = ReinforcementLearningAgent(
    actions=['increase', 'decrease', 'maintain', 'optimize'],
    use_gpu=True
)
print(f"Device: {agent.device}")
```

---

## Troubleshooting

### Issue: "CUDA not found"

**Solution**: Reinstall PyTorch with correct CUDA version:

```bash
pip uninstall torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### Issue: "nvidia-smi not found"

**Solution**: Install NVIDIA driver:

```bash
# On Ubuntu
sudo apt install nvidia-driver-525
sudo reboot
```

### Issue: "Docker GPU not working"

**Solution**: Ensure nvidia-docker is installed and running:

```bash
# Check docker runtime
docker info | grep -i nvidia

# If not configured, edit /etc/docker/daemon.json
sudo nano /etc/docker/daemon.json
```

Add:

```json
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

Then restart Docker:

```bash
sudo systemctl restart docker
```

---

## Performance Comparison

| Mode | RL Training Speed | Risk Analysis Speed |
| ----- | ----- | ----- |
| NumPy CPU | ~10 episodes/sec | ~1000 sim/sec |
| PyTorch CPU | ~50 episodes/sec | ~5000 sim/sec |
| PyTorch GPU | ~500 episodes/sec | ~50000 sim/sec |

---

## Additional Resources

- [PyTorch Official](https://pytorch.org/)
- [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads)
- [NVIDIA Docker](https://github.com/NVIDIA/nvidia-docker)

---

**Document Version:** 1.0
**Last Updated:** 2025
