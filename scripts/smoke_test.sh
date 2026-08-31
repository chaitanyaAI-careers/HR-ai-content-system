#!/bin/bash
set -e

echo "Running smoke checks..."

test -f app.py
test -d pipeline
test -d data
test -f requirements.txt
test -f README.md

echo "Smoke checks passed."
