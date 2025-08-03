# MongoDB Setup Guide for STAN Chatbot

## 🗄️ MongoDB Integration

Your STAN chatbot now supports **persistent data storage** using MongoDB, with automatic fallback to in-memory storage if MongoDB is not available.

## 📊 **What's Stored in MongoDB**

### **Collections:**
1. **`sessions`** - User conversation sessions
2. **`user_preferences`** - User settings and preferences

### **Session Data Structure:**
```json
{
  "_id": ObjectId("..."),
  "session_id": "user_123",
  "history": [
    {
      "timestamp": "2025-08-02T10:30:00",
      "user": "Hello!",
      "bot": "Hi there! I'm STAN, how can I help you?",
      "sentiment": "positive"
    }
  ],
  "created_at": ISODate("2025-08-02T10:30:00Z"),
  "last_active": ISODate("2025-08-02T10:35:00Z"),
  "message_count": 5,
  "user_info": {},
  "conversation_topics": ["greeting", "help"],
  "sentiment_history": ["positive", "neutral", "questioning"]
}
```

---

## 🚀 **Quick Start**

### **Option 1: Local MongoDB (Recommended for Development)**

1. **Install MongoDB:**
   ```bash
   # Windows
   Download from: https://www.mongodb.com/try/download/community
   
   # macOS
   brew install mongodb-community
   
   # Ubuntu/Debian
   sudo apt install mongodb
   ```

2. **Start MongoDB:**
   ```bash
   # Windows (if installed as service)
   # MongoDB starts automatically
   
   # macOS
   brew services start mongodb-community
   
   # Linux
   sudo systemctl start mongodb
   ```

3. **Verify Installation:**
   ```bash
   python test_mongodb.py
   ```

### **Option 2: No MongoDB (In-Memory Fallback)**

The chatbot automatically falls back to in-memory storage if MongoDB is not available. No setup required!

---

## 🏭 **Production Deployment Options**

### **MongoDB Atlas (Cloud) - Recommended for Production**

1. **Create Account:** [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

2. **Get Connection String:**
   ```
   mongodb+srv://username:password@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority
   ```

3. **Update Configuration:**
   ```python
   # In mongodb_config.py
   MONGODB_CONFIGS['production'] = MongoDBCloudConfig(
       username='your_username',
       password='your_password', 
       cluster='cluster0.abcde.mongodb.net'
   )
   ```

### **Docker MongoDB**

1. **Run MongoDB Container:**
   ```bash
   docker run -d --name mongodb -p 27017:27017 mongo:latest
   ```

2. **Update Configuration:**
   ```python
   # Use docker config
   config = get_config('docker')
   ```

### **Environment Variables**

Set environment variables for production:
```bash
export MONGODB_URI="mongodb+srv://user:pass@cluster.mongodb.net/"
export MONGODB_DATABASE="stan_chatbot_prod"
```

---

## 🔧 **Configuration Options**

### **Memory Manager Settings:**
```python
memory_manager = EnhancedMemoryManager(
    max_sessions=1000,              # Maximum sessions to store
    session_timeout_hours=24,       # Session expiry time
    mongodb_uri="mongodb://localhost:27017/"
)
```

### **Available Configurations:**
- **`local`** - Local MongoDB instance
- **`docker`** - Docker MongoDB container
- **`cloud`** - MongoDB Atlas cloud

---

## 📈 **Features & Benefits**

### **✅ Persistent Storage**
- Data survives server restarts
- Conversation history preserved
- User preferences maintained

### **✅ Scalability**
- Multiple server instances
- Horizontal scaling support
- Load balancer compatible

### **✅ Performance**
- Indexed queries for fast access
- Automatic cleanup of old sessions
- Optimized data structures

### **✅ Reliability**
- Automatic fallback to in-memory storage
- Error handling and logging
- Connection monitoring

---

## 🧪 **Testing**

### **Run Integration Tests:**
```bash
# Test MongoDB connection and features
python test_mongodb.py

# Test full API with MongoDB
python test_mongodb_api.py
```

### **API Endpoints:**
- **`/health`** - Health check with MongoDB status
- **`/stats`** - Session statistics
- **`/chat`** - Enhanced chat with sentiment analysis

---

## 🔍 **Monitoring**

### **Health Check:**
```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "storage_type": "MongoDB",
  "total_sessions": 42,
  "active_sessions": 15
}
```

### **Statistics:**
```bash
curl http://localhost:5000/stats
```

**Response:**
```json
{
  "total_sessions": 42,
  "active_sessions_last_hour": 15,
  "storage_type": "MongoDB"
}
```

---

## 🐛 **Troubleshooting**

### **Common Issues:**

1. **MongoDB Connection Failed:**
   ```
   ❌ MongoDB server not running or not installed
   ```
   **Solution:** Install and start MongoDB, or use in-memory fallback

2. **Permission Denied:**
   ```
   ❌ Authentication failed
   ```
   **Solution:** Check username/password in connection string

3. **Connection Timeout:**
   ```
   ❌ Server selection timeout
   ```
   **Solution:** Check network connectivity and firewall settings

### **Debug Mode:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📚 **Database Management**

### **View Data in MongoDB:**
```bash
# Connect to MongoDB shell
mongosh

# Switch to database
use stan_chatbot

# View sessions
db.sessions.find().pretty()

# View statistics
db.sessions.countDocuments()
```

### **Backup/Restore:**
```bash
# Backup
mongodump --db stan_chatbot --out ./backup

# Restore  
mongorestore --db stan_chatbot ./backup/stan_chatbot
```

---

## 🚀 **Ready for Production!**

Your STAN chatbot now features:
- ✅ **Persistent MongoDB storage**
- ✅ **Automatic fallback mechanism**
- ✅ **Enhanced sentiment analysis**
- ✅ **Empathetic response generation**
- ✅ **Context-aware conversations**
- ✅ **Session management and cleanup**
- ✅ **Production-ready monitoring**

**Start the enhanced chatbot:**
```bash
python app.py
```

**Test the integration:**
```bash
python test_mongodb_api.py
```
