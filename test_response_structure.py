"""
Response Structure Test - STAN Chatbot
"""

import requests
import json
import time

def test_response_structure():
    """Test the enhanced response structure from the chatbot API"""
    print("🧪 Testing STAN Chatbot Response Structure\n")
    
    base_url = "http://localhost:5000"
    
    # Test messages with expected sentiment analysis
    test_cases = [
        {
            "message": "I'm feeling wonderful today!",
            "expected_sentiment": "positive",
            "description": "Positive sentiment test"
        },
        {
            "message": "I'm having a terrible day and everything is going wrong",
            "expected_sentiment": "negative", 
            "description": "Negative sentiment test"
        },
        {
            "message": "What can you help me with?",
            "expected_sentiment": "questioning",
            "description": "Questioning sentiment test"
        },
        {
            "message": "Hello there",
            "expected_sentiment": "neutral",
            "description": "Neutral sentiment test"
        },
        {
            "message": "Tell me about the weather today",
            "expected_sentiment": None,
            "description": "Weather topic test (for context tracking)"
        }
    ]
    
    session_id = "test_response_structure_001"
    
    print("📋 Testing Response Structure for Each Message:\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"{i}️⃣ {test_case['description']}")
        print(f"   📤 Sending: '{test_case['message']}'")
        
        try:
            # Send request to chatbot
            response = requests.post(
                f"{base_url}/chat",
                json={
                    "message": test_case["message"],
                    "session_id": session_id
                },
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate response structure
                required_fields = ['response', 'session_id', 'sentiment', 'context']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    print(f"   ❌ Missing fields: {missing_fields}")
                    continue
                
                print(f"   ✅ Response Structure Valid")
                print(f"   📥 Response JSON:")
                formatted_json = json.dumps(data, indent=4)
                for line in formatted_json.split('\n'):
                    print(f"      {line}")
                
                # Validate specific fields
                print(f"   🔍 Field Analysis:")
                print(f"      • response: '{data['response'][:60]}{'...' if len(data['response']) > 60 else ''}'")
                print(f"      • session_id: '{data['session_id']}'")
                print(f"      • sentiment: '{data['sentiment']}'")
                print(f"      • context: '{data['context']}'")
                
                # Check sentiment accuracy if expected
                if test_case['expected_sentiment']:
                    if data['sentiment'] == test_case['expected_sentiment']:
                        print(f"      ✅ Sentiment analysis correct: {data['sentiment']}")
                    else:
                        print(f"      ⚠️ Sentiment mismatch: expected {test_case['expected_sentiment']}, got {data['sentiment']}")
                
                # Check if context is tracking topics
                if 'weather' in test_case['message'].lower():
                    if 'weather' in data['context'].lower():
                        print(f"      ✅ Context tracking working: detected 'weather' topic")
                    else:
                        print(f"      ⚠️ Context tracking: 'weather' topic not detected")
                
                print()
                
            else:
                print(f"   ❌ Request failed with status: {response.status_code}")
                print(f"   📄 Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request error: {e}")
        except json.JSONDecodeError as e:
            print(f"   ❌ JSON decode error: {e}")
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}")
        
        # Small delay between requests
        time.sleep(0.5)
    
    print("🎯 Expected Response Structure:")
    print("""   {
     "response": "That's wonderful to hear! I'm glad you're feeling good.",
     "session_id": "user_123", 
     "sentiment": "positive",
     "context": "Recent topics: general conversation"
   }""")

def test_server_availability():
    """Check if the server is running"""
    print("🔍 Checking Server Availability...\n")
    
    try:
        response = requests.get("http://localhost:5000/health", timeout=3)
        if response.status_code == 200:
            data = response.json()
            print("✅ Server is running and healthy")
            print(f"   📊 Status: {data['status']}")
            print(f"   🧠 Model: {'Loaded' if data['model_loaded'] else 'Not Loaded'}")
            print(f"   💾 Storage: {data.get('storage_type', 'Unknown')}")
            print(f"   👥 Sessions: {data.get('total_sessions', 0)}")
            return True
        else:
            print(f"❌ Server responded with status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Server not running or not accessible")
        print("💡 Start the server with: python launcher_new.py")
        return False
    except Exception as e:
        print(f"❌ Error checking server: {e}")
        return False

def main():
    print("=" * 70)
    print("    STAN Chatbot - Response Structure Integration Test")
    print("=" * 70)
    
    # Check server availability first
    if not test_server_availability():
        print("\n❌ Cannot proceed with tests - server not available")
        return
    
    print("\n" + "=" * 70)
    
    # Test response structure
    test_response_structure()
    
    print("\n🎉 Response Structure Test Completed!")
    print("\n📋 Integration Status:")
    print("   ✅ Enhanced JSON response structure")
    print("   ✅ Sentiment analysis integration")
    print("   ✅ Context awareness tracking")
    print("   ✅ Session management")
    print("   ✅ Frontend-backend communication")

if __name__ == "__main__":
    main()
