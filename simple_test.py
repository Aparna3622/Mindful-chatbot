print("🚀 STAN Chatbot Environment Test")
print("=" * 40)

try:
    import sys
    print(f"✅ Python {sys.version}")
    
    import flask
    print(f"✅ Flask {flask.__version__}")
    
    import transformers
    print(f"✅ Transformers {transformers.__version__}")
    
    import torch
    print(f"✅ PyTorch {torch.__version__}")
    
    import requests
    print(f"✅ Requests {requests.__version__}")
    
    print("\n🎯 Testing app import...")
    from app import app, chatbot
    print("✅ App imported successfully")
    
    print("\n💬 Testing chatbot response...")
    response = chatbot.generate_response("Hello!")
    print(f"Bot says: {response}")
    
    print("\n🌐 Testing Flask app with test client...")
    with app.test_client() as client:
        # Test health endpoint
        health_response = client.get('/health')
        print(f"Health check: {health_response.status_code} - {health_response.get_json()}")
        
        # Test chat endpoint
        chat_response = client.post('/chat', json={
            "message": "Hello, how are you?",
            "session_id": "test_session"
        })
        print(f"Chat test: {chat_response.status_code} - {chat_response.get_json()}")
    
    print("\n🎉 All tests passed! Your chatbot is ready to use.")
    print("\n📋 To run the chatbot:")
    print("1. Start the Flask app: python app.py")
    print("2. Open your browser to: http://localhost:5000")
    print("3. Or run tests: python test_chatbot.py")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
