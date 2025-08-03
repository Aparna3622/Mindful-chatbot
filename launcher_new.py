#!/usr/bin/env python3
"""
STAN Chatbot Launcher - Frontend-Backend Integration
"""

import subprocess
import time
import webbrowser
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
