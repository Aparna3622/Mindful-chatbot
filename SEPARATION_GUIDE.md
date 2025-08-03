# STAN Chatbot - Repository Separation Guide

## 🔄 How to Separate Files from Your GitHub Repository

Since you've uploaded the entire project to GitHub (Mindful-chatbot), here's how to create separate frontend and backend deployments:

### Method 1: Create Two New Repositories (Recommended)

#### Backend Repository Setup

1. **Create new GitHub repository:** `stan-chatbot-backend`

2. **Copy these files from your main repo:**
   ```
   stan_chatbot/app_backend_only.py → app.py
   stan_chatbot/requirements_backend.txt → requirements.txt
   ```

3. **Files to include in backend repo:**
   ```
   stan-chatbot-backend/
   ├── app.py (renamed from app_backend_only.py)
   ├── requirements.txt 
   ├── README.md
   └── Procfile (for Heroku)
   ```

4. **Create Procfile for deployment:**
   ```
   web: python app.py
   ```

#### Frontend Repository Setup

1. **Create new GitHub repository:** `stan-chatbot-frontend`

2. **Copy these files from your main repo:**
   ```
   stan_chatbot/frontend_standalone.html → index.html
   ```

3. **Update the API URL in index.html:**
   ```javascript
   // Line 87 in index.html
   API_BASE_URL: 'https://your-backend-app.railway.app'
   ```

4. **Files to include in frontend repo:**
   ```
   stan-chatbot-frontend/
   ├── index.html
   ├── README.md
   └── vercel.json (optional)
   ```

### Method 2: Use GitHub Actions to Auto-Split (Advanced)

Create GitHub Actions to automatically deploy from subdirectories:

#### Backend Deployment Action
```yaml
# .github/workflows/deploy-backend.yml
name: Deploy Backend
on:
  push:
    paths: ['stan_chatbot/app_backend_only.py', 'stan_chatbot/requirements_backend.txt']
    
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Railway
        # Railway deployment steps
```

#### Frontend Deployment Action  
```yaml
# .github/workflows/deploy-frontend.yml
name: Deploy Frontend
on:
  push:
    paths: ['stan_chatbot/frontend_standalone.html']
    
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        # Vercel deployment steps
```

### Method 3: Platform-Specific Import (Easiest)

#### Railway Backend Import:
1. **Connect to GitHub:** Select `Mindful-chatbot` repository
2. **Set Root Directory:** `stan_chatbot/`
3. **Set Start Command:** `python app_backend_only.py`
4. **Set Build Command:** `pip install -r requirements_backend.txt`

#### Vercel Frontend Import:
1. **Connect to GitHub:** Select `Mindful-chatbot` repository  
2. **Set Root Directory:** `stan_chatbot/`
3. **Framework:** Other
4. **Build Command:** Leave empty (static)
5. **Output Directory:** `./` 
6. **Install Command:** Leave empty

### Quick Commands for File Separation:

```bash
# Clone your existing repo
git clone https://github.com/Aparna3622/Mindful-chatbot.git
cd Mindful-chatbot

# Create backend repo
mkdir ../stan-backend
cp stan_chatbot/app_backend_only.py ../stan-backend/app.py
cp stan_chatbot/requirements_backend.txt ../stan-backend/requirements.txt
echo "web: python app.py" > ../stan-backend/Procfile

# Create frontend repo  
mkdir ../stan-frontend
cp stan_chatbot/frontend_standalone.html ../stan-frontend/index.html

# Initialize git repos
cd ../stan-backend && git init
cd ../stan-frontend && git init
```

### Deployment URLs After Separation:

- **Backend:** `https://your-backend.railway.app`
- **Frontend:** `https://your-frontend.vercel.app`

### Update Frontend Configuration:

After backend deployment, update line 87 in `index.html`:
```javascript
API_BASE_URL: 'https://YOUR-ACTUAL-BACKEND-URL.railway.app'
```

## 🚀 Recommended Workflow:

1. **Deploy Backend First** (Railway/Heroku)
2. **Get Backend URL** 
3. **Update Frontend** with backend URL
4. **Deploy Frontend** (Vercel/Netlify)
5. **Test Connection**

This gives you professional separation with optimal performance! 🎯
