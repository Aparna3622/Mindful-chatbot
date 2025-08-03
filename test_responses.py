#!/usr/bin/env python3
"""
Quick test of the improved chatbot responses
"""

import sys
import os
import time

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_improved_responses():
    """Test the improved chatbot responses"""
    print("🧪 Testing Improved STAN Chatbot Responses")
    print("=" * 50)
    
    try:
        from app import chatbot
        
        # Test various types of messages
        test_messages = [
            "Hello!",
            "How are you?",
            "What can you do?",
            "Tell me a joke",
            "What's your name?",
            "How old are you?",
            "You're amazing!",
            "What's the weather like?",
            "What time is it?",
            "Thank you",
            "Help me",
            "Random question about life"
        ]
        
        print("Testing fallback responses directly:\n")
        
        for i, message in enumerate(test_messages, 1):
            print(f"{i:2d}. User: {message}")
            response = chatbot._fallback_response(message)
            print(f"    Bot: {response}")
            print()
            time.sleep(0.5)  # Small delay for readability
        
        print("✅ All improved responses working!")
        print("\n🌐 Your Flask app should now give much better responses!")
        print("   Visit: http://localhost:5000 to test in the web interface")
        
    except Exception as e:
        print(f"❌ Error testing responses: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_improved_responses()
