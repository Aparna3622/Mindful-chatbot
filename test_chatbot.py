#!/usr/bin/env python3
"""
Test script for STAN Chatbot
"""

import sys
import subprocess
import json
import time

# Install requests if not available
try:
    import requests
except ImportError:
    print("📦 Installing requests library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def test_chatbot():
    """Test the chatbot functionality"""
    base_url = "http://localhost:5000"
    
    # Test health endpoint
    print("🔍 Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Health check passed: {health_data}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to server: {e}")
        print("💡 Make sure the Flask app is running: python app.py")
        return False
    
    # Test chat endpoint
    print("\n💬 Testing chat functionality...")
    test_messages = [
        "Hello!",
        "How are you?",
        "What can you do?",
        "Tell me a joke",
        "Thank you!",
        "Goodbye"
    ]
    
    session_id = "test_session_" + str(int(time.time()))
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n{i}. User: {message}")
        
        try:
            response = requests.post(
                f"{base_url}/chat",
                json={
                    "message": message,
                    "session_id": session_id
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                bot_response = data.get('response', 'No response')
                print(f"   Bot: {bot_response}")
                time.sleep(1)  # Small delay between messages
            else:
                print(f"   ❌ Error: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
    
    print("\n✅ Chat test completed!")
    return True

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n🧪 Testing edge cases...")
    base_url = "http://localhost:5000"
    
    # Test empty message
    print("Testing empty message...")
    response = requests.post(
        f"{base_url}/chat",
        json={"message": "", "session_id": "test"},
        timeout=5
    )
    print(f"Empty message response: {response.status_code}")
    
    # Test very long message
    print("Testing long message...")
    long_message = "This is a very long message. " * 100
    response = requests.post(
        f"{base_url}/chat",
        json={"message": long_message, "session_id": "test"},
        timeout=30
    )
    print(f"Long message response: {response.status_code}")
    
    # Test special characters
    print("Testing special characters...")
    special_message = "Hello! @#$%^&*()_+ 🤖💬🎉"
    response = requests.post(
        f"{base_url}/chat",
        json={"message": special_message, "session_id": "test"},
        timeout=10
    )
    print(f"Special characters response: {response.status_code}")

if __name__ == "__main__":
    print("🚀 STAN Chatbot Test Suite")
    print("=" * 40)
    
    if test_chatbot():
        test_edge_cases()
        print("\n🎉 All tests completed!")
    else:
        print("\n❌ Tests failed!")
        exit(1)
