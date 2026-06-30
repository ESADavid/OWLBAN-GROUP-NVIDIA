# NVIDIA NGC Private Registry Setup Guide

This guide provides instructions for setting up the NVIDIA NGC Private Registry for OWLBAN GROUP AI. The NGC private registry allows access to NVIDIA AI containers, models, and tools.

## Prerequisites

Before starting, ensure you have:

1. **NVIDIA NGC Account**: Create one at https://ngc.nvidia.com/
2. **NGC API Key**: Generate at https://ngc.nvidia.com/setup/api-key
3. **Docker**: Installed and running
4. **Git**: Installed

## Quick Setup

### Step 1: Set Environment Variable

```bash
# Linux/macOS
export NGC_API_KEY='your-api-key-here'

# Windows (Command Prompt)
set NGC_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:NGC_API_KEY='your-api-key-here'
```

### Step 2: Run Setup Script

```bash
# On Linux/macOS
chmod +x ngc/setup.sh
./ngc/setup.sh

# On Windows, run the commands manually from ngc/setup.sh
```

### Step 3: Test Docker Login

```bash
echo $NGC_API_KEY | docker login nvcr.io -u $oauthtoken --password-stdin
```

## Manual Setup

### Docker Registry Authentication

1. Create Docker config directory:
```bash
mkdir -p ~/.docker
```

2. Create Docker config file with NGC credentials:
```bash
# Create ~/.docker/config.json with the following content:
{
  "auths": {
    "nvcr.io": {
      "username": "$oauthtoken",
      "password": "YOUR_NGC_API_KEY",
      "email": "your-email@example.com"
    }
  }
}
```

### NGC CLI Installation

1. Download NGC CLI:
```bash
# Linux/macOS
curl -s https://api.ngc.nvidia.com/download/ngc-cli/ngccli -o ngc.zip
unzip -q ngc.zip

# Windows
# Use the Windows installer from https://ngc.nvidia.com/resources
```

2. Add to PATH:
```bash
# Linux/macOS (add to ~/.bashrc or ~/.zshrc)
export PATH=~/ngc-cli/ngc:$PATH

# Windows
# Add to System Environment Variables -> Path
```

3. Configure NGC CLI:
```bash
ngc config set ngc_api_key YOUR_NGC_API_KEY
```

## Pulling Private Images

Once authenticated, you can pull private NGC images:

```bash
# Example: Pull Triton Inference Server
docker pull nvcr.io/nvidia/tritonserver:23.10-py3

# Example: Pull a specific container
docker pull nvcr.io/nvidia/ai-workflow:latest
```

## Using with Docker Compose

The project includes pre-configured services that use NGC images:

```bash
# Start services with NVIDIA GPU support
docker-compose up -d triton-server

# View running services
docker-compose ps
```

## Environment Variables

The following environment variables are used:

| Variable | Description |
|----------|-------------|
| `NGC_API_KEY` | Your NGC API key |
| `DOCKER_CONFIG` | Path to Docker config (default: `ngc/docker`) |

## Troubleshooting

### Login Failed

1. Verify your API key is correct
2. Check API key hasn't expired
3. Ensure you have access to the private registry

### Image Pull Failed

1. Verify Docker authentication: `docker login nvcr.io`
2. Check your NGC org/team permissions
3. Ensure the image name is correct

### Permission Denied

1. Check Docker daemon is running
2. Verify you have Docker group permissions
3. Try with sudo (development only)

## Integration with Project

The project uses NGC private registry for:

1. **Triton Inference Server**: `nvcr.io/nvidia/tritonserver:23.10-py3`
2. **CUDA Base Images**: `nvidia/cuda:12.2-runtime-ubuntu22.04`
3. **Additional AI Containers**: Various NVIDIA AI containers

## Security Best Practices

1. **Never commit API keys** to version control
2. Use environment variables or secrets management
3. Rotate API keys periodically
4. Use read-only tokens when possible

## Additional Resources

- [NGC Documentation](https://docs.nvidia.com/ngc/)
- [NGC User Guide](https://docs.nvidia.com/ngc/latest/ngc-private-registry-user-guide.html)
- [Triton Inference Server Documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/)

## Support

For issues or questions:
1. Check NVIDIA GPU Cloud documentation
2. Contact your NVIDIA enterprise representative
3. Submit support tickets through NGC portal
