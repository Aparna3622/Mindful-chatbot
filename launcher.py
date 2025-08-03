#!/usr/bin/env python3
"""
STAN Chatbot Launcher
This script starts the Flask app and runs tests
"""

import sys
import subprocess
import time
import os
import threading
import signal

def start_flask_app():
    """Start the Flask application"""
    print("🚀 Starting Flask application...")
    try:
        # Start Flask app in a subprocess
        process = subprocess.Popen([
            sys.executable, "app.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Give the app time to start
        time.sleep(3)
        
        return process
    except Exception as e:
        print(f"❌ Failed to start Flask app: {e}")
        return None

def run_tests():
    """Run the test script"""
    #!/usr/bin/env python3
"""
STAN Chatbot Launcher - Frontend-Backend Integration
"""

import subprocess
import time
import webbrowser
import requests
import sys
import os

def main():
    print("🚀 Starting STAN Chatbot with Frontend-Backend Integration")
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Start the Flask server
    print("Starting Flask server...")
    try:
        # Run the app directly
        import app
        print("✅ App imported successfully")
        print("✅ Enhanced features loaded (sentiment analysis, context awareness)")
        print("✅ MongoDB fallback to in-memory storage")
        print()
        print("🌐 Starting web server on http://localhost:5000")
        print("💡 Frontend-Backend Integration Features:")
        print("   • Real-time sentiment analysis")
        print("   • Context-aware conversations") 
        print("   • Session management")
        print("   • Connection status monitoring")
        print("   • Empathetic response generation")
        print()
        print("🎯 Opening browser in 3 seconds...")
        
        # Wait a moment then open browser
        time.sleep(3)
        webbrowser.open("http://localhost:5000")
        
        # Start the Flask app
        app.app.run(debug=True, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print()
        print()
        print("🛑 Shutting down STAN Chatbot...")
        print("👋 Thanks for using STAN!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
    try:
        result = subprocess.run([
            sys.executable, "test_chatbot.py"
        ], capture_output=True, text=True, timeout=60)
        
        print("STDOUT:")
        print(result.stdout)
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
            
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("❌ Tests timed out")
        return False
    except Exception as e:
        print(f"❌ Failed to run tests: {e}")
        return False

def main():
    """Main function"""
    print("🎯 STAN Chatbot Launcher")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ app.py not found. Please run this script from the chatbot directory.")
        return
    
    # Start Flask app
    flask_process = start_flask_app()
    if not flask_process:
        return
    
    try:
        # Run tests
        success = run_tests()
        
        if success:
            print("\n✅ All tests passed!")
        else:
            print("\n❌ Some tests failed!")
            
    finally:
        # Clean up
        print("\n🧹 Cleaning up...")
        try:
            flask_process.terminate()
            flask_process.wait(timeout=5)
        except:
            flask_process.kill()
        print("✅ Flask app stopped")

if __name__ == "__main__":
    main()
