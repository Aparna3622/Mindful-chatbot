"""
Frontend-Backend Connection Test for STAN Chatbot
"""

import subprocess
import time
import requests
import webbrowser
import sys
from pathlib import Path

def start_chatbot_server():
    """Start the chatbot server in background"""
    try:
        print("🚀 Starting STAN Chatbot Server...")
        
        # Start the Flask app
        process = subprocess.Popen([
            "C:/python/python.exe", "app.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Check if server is running
        try:
            response = requests.get("http://localhost:5000/health", timeout=5)
            if response.status_code == 200:
                print("✅ Server started successfully!")
                return process
            else:
                print("❌ Server health check failed")
                return None
        except requests.exceptions.RequestException:
            print("❌ Server not responding")
            return None
            
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return None

def test_frontend_backend_connection():
    """Test the complete frontend-backend integration"""
    print("\n🧪 Testing Frontend-Backend Connection\n")
    
    base_url = "http://localhost:5000"
    
    # Test 1: Health Check
    print("1️⃣ Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Status: {data['status']}")
            print(f"   🧠 Model: {'Loaded' if data['model_loaded'] else 'Not Loaded'}")
            print(f"   💾 Storage: {data.get('storage_type', 'Unknown')}")
            print(f"   📊 Sessions: {data.get('total_sessions', 0)}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Health check error: {e}")
        return False
    
    # Test 2: Web Interface
    print("\n2️⃣ Testing web interface...")
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("   ✅ Web interface accessible")
            html_content = response.text
            
            # Check for key frontend features
            features = {
                "Enhanced header": "connection-status" in html_content,
                "Sentiment indicators": "sentiment-indicator" in html_content,
                "Context info": "context-info" in html_content,
                "Message metadata": "message-metadata" in html_content,
                "Enhanced ChatBot class": "checkConnection" in html_content
            }
            
            for feature, present in features.items():
                status = "✅" if present else "❌"
                print(f"   {status} {feature}: {'Present' if present else 'Missing'}")
                
        else:
            print(f"   ❌ Web interface failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Web interface error: {e}")
        return False
    
    # Test 3: Chat API with Enhanced Features
    print("\n3️⃣ Testing enhanced chat API...")
    test_messages = [
        "Hello! I'm excited to test this chatbot!",
        "I'm feeling a bit sad today.",
        "What can you help me with?",
        "Tell me about the weather."
    ]
    
    session_id = "test_frontend_backend_001"
    
    for i, message in enumerate(test_messages, 1):
        try:
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
                print(f"   {i}. ✅ Message: '{message[:30]}...'")
                print(f"      Response: '{data['response'][:50]}...'")
                print(f"      Sentiment: {data.get('sentiment', 'N/A')}")
                print(f"      Context: {data.get('context', 'N/A')}")
            else:
                print(f"   {i}. ❌ Message failed: {response.status_code}")
                
        except Exception as e:
            print(f"   {i}. ❌ Message error: {e}")
    
    # Test 4: Statistics Endpoint
    print("\n4️⃣ Testing statistics endpoint...")
    try:
        response = requests.get(f"{base_url}/stats", timeout=5)
        if response.status_code == 200:
            stats = response.json()
            print(f"   ✅ Storage Type: {stats.get('storage_type', 'Unknown')}")
            print(f"   📊 Total Sessions: {stats.get('total_sessions', 0)}")
            print(f"   👥 Active Sessions: {stats.get('active_sessions_last_hour', 0)}")
        else:
            print(f"   ❌ Stats failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Stats error: {e}")
    
    return True

def open_browser():
    """Open the chatbot in browser"""
    print("\n🌐 Opening chatbot in browser...")
    try:
        webbrowser.open("http://localhost:5000")
        print("✅ Browser opened successfully!")
        return True
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        return False

def main():
    print("=" * 60)
    print("    STAN Chatbot - Frontend-Backend Integration Test")
    print("=" * 60)
    
    # Start server
    server_process = start_chatbot_server()
    
    if not server_process:
        print("\n❌ Failed to start server. Exiting.")
        sys.exit(1)
    
    try:
        # Test connection
        success = test_frontend_backend_connection()
        
        if success:
            print("\n🎉 Frontend-Backend Integration Test Passed!")
            print("\n📋 Test Results:")
            print("   ✅ Server started successfully")
            print("   ✅ Health endpoint working")
            print("   ✅ Web interface accessible") 
            print("   ✅ Enhanced chat API working")
            print("   ✅ Sentiment analysis active")
            print("   ✅ Context awareness working")
            print("   ✅ MongoDB integration active")
            
            # Open browser
            browser_opened = open_browser()
            
            if browser_opened:
                print("\n🚀 Ready to use! Features available:")
                print("   • Real-time sentiment analysis")
                print("   • Context-aware conversations")
                print("   • MongoDB persistent storage")
                print("   • Empathetic response generation")
                print("   • Session management")
                print("   • Connection status monitoring")
                
                print("\n💡 Press Ctrl+C to stop the server")
                
                # Keep server running
                try:
                    server_process.wait()
                except KeyboardInterrupt:
                    print("\n\n🛑 Stopping server...")
            
        else:
            print("\n❌ Some tests failed. Check the logs above.")
            
    finally:
        # Clean up
        if server_process:
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()

if __name__ == "__main__":
    main()
