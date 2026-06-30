#!/bin/bash
# NGC Private Registry Setup Script for OWLBAN GROUP AI
# This script sets up NGC CLI and Docker registry authentication

set -e

echo "=== OWLBAN GROUP AI - NGC Private Registry Setup ==="

# Check if NGC_API_KEY is set
if [ -z "$NGC_API_KEY" ]; then
    echo "Error: NGC_API_KEY environment variable is not set"
    echo "Please set your NGC API key:"
    echo "  export NGC_API_KEY='your-api-key-here'"
    exit 1
fi

# Create NGC config directory if it doesn't exist
mkdir -p ~/.docker
mkdir -p ngc/docker

# Setup Docker registry authentication
echo "Setting up Docker registry authentication..."
export DOCKER_CONFIG=ngc/docker

# Create Docker config.json with NGC credentials
cat > ngc/docker/config.json << EOF
{
  "auths": {
    "nvcr.io": {
      "username": "\$oauthtoken",
      "password": "${NGC_API_KEY}",
      "email": "owlban-group@ai.com"
    }
  }
}
EOF

echo "Docker config created at ngc/docker/config.json"

# Copy Docker config to home directory
cp ngc/docker/config.json ~/.docker/config.json

# Set proper permissions
chmod 600 ngc/docker/config.json
chmod 600 ~/.docker/config.json

# Test Docker login (optional - will work if credentials are valid)
echo "Testing Docker login to nvcr.io..."
echo "$NGC_API_KEY" | docker login nvcr.io -u "$oauthtoken" --password-stdin 2>/dev/null || echo "Note: Docker login test skipped"

# Install NGC CLI if not present
if ! command -v ngc &> /dev/null; then
    echo "Installing NGC CLI..."
    cd /tmp
    curl -s https://api.ngc.nvidia.com/download/ngc-cli/ngccli -o ngc.zip
    unzip -q ngc.zip
    mkdir -p ~/ngc-cli
    mv ngc ~/ngc-cli/
    export PATH=~/ngc-cli/ngc:$PATH
    echo "NGC CLI installed. Add to PATH: export PATH=~/ngc-cli/ngc:\$PATH"
    cd - > /dev/null
else
    echo "NGC CLI already installed"
fi

# Configure NGC CLI
echo "Configuring NGC CLI..."
ngc config set ngc_api_key $NGC_API_KEY 2>/dev/null || echo "NGC CLI configuration skipped"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To use NGC private registry:"
echo "1. Ensure NGC_API_KEY is set: export NGC_API_KEY='your-key'"
echo "2. Use Docker with private images: docker pull nvcr.io/..."
echo "3. For NGC CLI: ngc <command>"
echo ""
