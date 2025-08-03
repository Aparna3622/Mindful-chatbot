// Frontend Configuration for STAN Chatbot
const CONFIG = {
    // Production backend URL (update after backend deployment)
    API_BASE_URL: 'https://your-backend.railway.app',
    
    // Local development URL
    // API_BASE_URL: 'http://localhost:5000',
    
    // API endpoints
    ENDPOINTS: {
        CHAT: '/chat',
        HEALTH: '/health', 
        STATS: '/stats',
        DATA: '/data'
    },
    
    // UI settings
    MAX_MESSAGE_LENGTH: 500,
    TYPING_DELAY: 1000,
    
    // Session settings
    SESSION_TIMEOUT: 30 * 60 * 1000, // 30 minutes
};

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
