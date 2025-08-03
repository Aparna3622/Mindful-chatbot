#!/usr/bin/env python3
"""
Simple test to check if the environment is working
"""

import sys
import os

print("🔍 Environment Check")
print("=" * 30)
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")

try:
    import flask
    print(f"✅ Flask version: {flask.__version__}")
except ImportError:
    print("❌ Flask not installed")

try:
    import transformers
    print(f"✅ Transformers version: {transformers.__version__}")
except ImportError:
    print("❌ Transformers not installed")

try:
    import torch
    print(f"✅ PyTorch version: {torch.__version__}")
except ImportError:
    print("❌ PyTorch not installed")

try:
    import requests
    print(f"✅ Requests version: {requests.__version__}")
except ImportError:
    print("❌ Requests not installed")

print("\n🎯 Starting Flask app test...")
if __name__ == "__main__":
    from app import app
    print("✅ App imported successfully")
    print("🚀 Starting Flask development server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
