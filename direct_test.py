#!/usr/bin/env python3
"""
Direct test of the chatbot functionality without requiring a separate server
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required libraries can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import flask
        print(f"✅ Flask {flask.__version__}")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        import transformers
        print(f"✅ Transformers {transformers.__version__}")
    except ImportError as e:
        print(f"❌ Transformers import failed: {e}")
        return False
    
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
    except ImportError as e:
        print(f"❌ PyTorch import failed: {e}")
        return False
    
    try:
        import requests
        print(f"✅ Requests {requests.__version__}")
    except ImportError as e:
        print(f"❌ Requests import failed: {e}")
        return False
    
    return True

def test_app_import():
    """Test if the app can be imported"""
    print("\n🔍 Testing app import...")
    
    try:
        from app import app, chatbot
        print("✅ App imported successfully")
        return app, chatbot
    except Exception as e:
        print(f"❌ App import failed: {e}")
        return None, None

def test_chatbot_directly(chatbot):
    """Test the chatbot functionality directly"""
    print("\n💬 Testing chatbot directly...")
    
    test_messages = [
        "Hello!",
        "How are you?",
        "What can you do?",
        "Tell me a joke",
        "Thank you!"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n{i}. User: {message}")
        try:
            # Test the chatbot function directly
            response = chatbot.generate_response(message)
            print(f"   Bot: {response}")
        except Exception as e:
            print(f"   ❌ Error: {e}")

def test_flask_routes(app):
    """Test Flask routes using test client"""
    print("\n🌐 Testing Flask routes...")
    
    with app.test_client() as client:
        # Test health endpoint
        print("Testing /health endpoint...")
        response = client.get('/health')
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.get_json()}")
        
        # Test chat endpoint
        print("\nTesting /chat endpoint...")
        test_data = {
            "message": "Hello, how are you?",
            "session_id": "test_session"
        }
        response = client.post('/chat', 
                              json=test_data,
                              content_type='application/json')
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.get_json()}")
        else:
            print(f"Error: {response.data}")

def main():
    """Main test function"""
    print("🚀 STAN Chatbot Direct Test Suite")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed!")
        return
    
    # Test app import
    app, chatbot = test_app_import()
    if not app or not chatbot:
        print("\n❌ App import failed!")
        return
    
    # Test chatbot directly
    test_chatbot_directly(chatbot)
    
    # Test Flask routes
    test_flask_routes(app)
    
    print("\n🎉 All direct tests completed!")

if __name__ == "__main__":
    main()
