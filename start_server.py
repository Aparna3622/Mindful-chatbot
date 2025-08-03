"""
Simple Server Starter for Testing
"""
import subprocess
import sys
import time

def start_server():
    """Start the Flask server for testing"""
    print("🚀 Starting STAN Chatbot Server for Testing...")
    
    try:
        # Import and run lightweight version
        import app_lightweight as app
        print("✅ Lightweight app imported successfully")
        print("✅ Starting Flask server...")
        print("🌐 Server will be available at: http://localhost:5000")
        print("💡 Press Ctrl+C to stop the server")
        
        # Start Flask app
        app.app.run(debug=True, host='127.0.0.1', port=5000)
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        
if __name__ == "__main__":
    start_server()
