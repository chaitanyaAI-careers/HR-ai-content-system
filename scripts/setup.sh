#!/bin/bash
set -e

echo "Setting up hr-ai-content-system..."

if [ ! -d "venv" ] && [ ! -d ".venv" ]; then
  python3 -m venv venv
fi

if [ -d "venv" ]; then
  source venv/bin/activate
elif [ -d ".venv" ]; then
  source .venv/bin/activate
fi

pip install --upgrade pip
pip install -r requirements.txt

mkdir -p docs tests/unit tests/integration scripts infra logs

echo "Setup complete."
