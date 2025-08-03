# STAN Chatbot Frontend - Deployment Ready

## 📁 Frontend Files for Separate Deployment

### Required Files:

1. **`index.html`** - Main frontend file (rename from frontend_standalone.html)
2. **`config.js`** - Configuration file  
3. **`vercel.json`** - Vercel deployment config (optional)
4. **`netlify.toml`** - Netlify deployment config (optional)

### Frontend Repository Structure:

```
stan-chatbot-frontend/
├── index.html          # Main chat interface
├── config.js           # API configuration
├── README.md           # Frontend documentation
├── vercel.json         # Vercel config (optional)
└── netlify.toml        # Netlify config (optional)
```

### Deployment Options:

#### Option 1: Vercel (Recommended)
- Perfect for static sites
- Automatic HTTPS
- Global CDN
- Easy GitHub integration

#### Option 2: Netlify  
- Great for static sites
- Drag & drop deployment
- Form handling capabilities

#### Option 3: GitHub Pages
- Free hosting
- Direct from repository
- Custom domain support

#### Option 4: Surge.sh
- Simple CLI deployment
- Fast setup
- Custom domains

### Quick Deployment Commands:

#### Vercel:
```bash
npm i -g vercel
vercel --prod
```

#### Netlify:
```bash
npm i -g netlify-cli
netlify deploy --prod
```

#### Surge:
```bash
npm i -g surge
surge
```

### Important: Update Backend URL

After backend deployment, update the API URL in your frontend:

```javascript
// In index.html or config.js
const CONFIG = {
    API_BASE_URL: 'https://your-backend.railway.app'
};
```

### Files Ready for Frontend Deployment:

1. **`frontend_standalone.html`** - Complete standalone frontend
2. **`templates/index.html`** - Original integrated version

Choose `frontend_standalone.html` for separate deployment!
