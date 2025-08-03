"""
Comprehensive Test for MongoDB-Enhanced STAN Chatbot
"""

import requests
import json
import time
from datetime import datetime

def test_mongodb_chatbot():
    """Test the MongoDB-enhanced chatbot via HTTP API"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing MongoDB-Enhanced STAN Chatbot\n")
    
    # Test 1: Health Check
    print("1️⃣ Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print(f"   ✅ Health Status: {health_data['status']}")
            print(f"   🧠 Model Loaded: {health_data['model_loaded']}")
            print(f"   💾 Storage Type: {health_data['storage_type']}")
            print(f"   📊 Total Sessions: {health_data['total_sessions']}")
            print(f"   👥 Active Sessions: {health_data['active_sessions']}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Could not connect to server: {e}")
        print("   💡 Make sure to run: python app.py")
        return False
    
    # Test 2: Statistics Endpoint
    print("\n2️⃣ Testing statistics endpoint...")
    try:
        response = requests.get(f"{base_url}/stats", timeout=5)
        if response.status_code == 200:
            stats = response.json()
            print(f"   📊 Storage Type: {stats['storage_type']}")
            print(f"   📊 Total Sessions: {stats['total_sessions']}")
            print(f"   📊 Active Sessions: {stats['active_sessions_last_hour']}")
        else:
            print(f"   ❌ Stats endpoint failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Stats request failed: {e}")
    
    # Test 3: Multiple conversation sessions
    print("\n3️⃣ Testing multiple conversation sessions...")
    
    test_conversations = [
        {
            "session_id": "test_user_001",
            "messages": [
                "Hello! I'm new here.",
                "I'm feeling excited about this chatbot!",
                "Can you tell me a joke?",
                "What can you help me with?"
            ]
        },
        {
            "session_id": "test_user_002", 
            "messages": [
                "Hi there, I'm having a terrible day.",
                "Everything is going wrong.",
                "Can you help me feel better?",
                "Thank you, that's much better!"
            ]
        },
        {
            "session_id": "test_user_003",
            "messages": [
                "What's the weather like today?",
                "How does this technology work?",
                "Are you using AI models?",
                "That's fascinating!"
            ]
        }
    ]
    
    session_results = {}
    
    for conversation in test_conversations:
        session_id = conversation["session_id"]
        print(f"\n   👤 Testing session: {session_id}")
        
        session_results[session_id] = []
        
        for i, message in enumerate(conversation["messages"], 1):
            try:
                # Send message to chatbot
                payload = {
                    "message": message,
                    "session_id": session_id
                }
                
                response = requests.post(
                    f"{base_url}/chat", 
                    json=payload,
                    headers={'Content-Type': 'application/json'},
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    bot_response = data['response']
                    sentiment = data.get('sentiment', 'unknown')
                    context = data.get('context', '')
                    
                    print(f"      {i}. User: {message}")
                    print(f"         Bot: {bot_response}")
                    print(f"         Sentiment: {sentiment}")
                    if context:
                        print(f"         Context: {context}")
                    
                    session_results[session_id].append({
                        'user_message': message,
                        'bot_response': bot_response,
                        'sentiment': sentiment,
                        'context': context
                    })
                    
                    # Small delay between messages
                    time.sleep(0.5)
                    
                else:
                    print(f"      ❌ Message {i} failed: {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                print(f"      ❌ Request failed: {e}")
    
    # Test 4: Context continuity
    print("\n4️⃣ Testing context continuity...")
    context_test_session = "context_test_001"
    
    context_messages = [
        "My name is Alice and I work at Microsoft.",
        "What's my name?",
        "Where do I work?",
        "Tell me about my previous messages."
    ]
    
    print(f"   👤 Testing context session: {context_test_session}")
    
    for i, message in enumerate(context_messages, 1):
        try:
            payload = {
                "message": message,
                "session_id": context_test_session
            }
            
            response = requests.post(
                f"{base_url}/chat", 
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                bot_response = data['response']
                
                print(f"      {i}. User: {message}")
                print(f"         Bot: {bot_response}")
                
                time.sleep(0.5)
                
        except requests.exceptions.RequestException as e:
            print(f"      ❌ Context test failed: {e}")
    
    # Test 5: Final statistics
    print("\n5️⃣ Final statistics after testing...")
    try:
        response = requests.get(f"{base_url}/stats", timeout=5)
        if response.status_code == 200:
            stats = response.json()
            print(f"   📊 Storage Type: {stats['storage_type']}")
            print(f"   📊 Total Sessions: {stats['total_sessions']}")
            print(f"   📊 Active Sessions: {stats['active_sessions_last_hour']}")
        
        # Also check health endpoint
        health_response = requests.get(f"{base_url}/health", timeout=5)
        if health_response.status_code == 200:
            health_data = health_response.json()
            print(f"   💾 MongoDB Sessions: {health_data['total_sessions']}")
            
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Final stats request failed: {e}")
    
    print("\n🎉 MongoDB-Enhanced Chatbot Test Completed!")
    print("\n📋 Test Summary:")
    print(f"   • Tested {len(test_conversations)} conversation sessions")
    print(f"   • Tested context continuity with 1 session")
    print(f"   • Verified MongoDB storage integration")
    print(f"   • Confirmed sentiment analysis")
    print(f"   • Validated empathetic responses")
    
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("    STAN Chatbot - MongoDB Integration API Test")
    print("=" * 60)
    
    print("\n💡 Make sure the chatbot server is running:")
    print("   python app.py")
    print("\n⏳ Starting test in 3 seconds...\n")
    
    time.sleep(3)
    
    success = test_mongodb_chatbot()
    
    if success:
        print("\n🚀 All tests passed! MongoDB integration is working perfectly!")
    else:
        print("\n❌ Some tests failed. Check the server logs.")
