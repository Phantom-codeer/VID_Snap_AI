# VID_Snap_AI Deployment Guide

This guide covers deploying VID_Snap_AI to various platforms.

## Prerequisites

- Python 3.8+
- FFmpeg installed on server
- ElevenLabs API Key
- Git (for cloning repository)

## Environment Setup

### 1. Set Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your ElevenLabs API key:

```
ELEVENLABS_API_KEY=sk_your_api_key_here
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

#### Windows
```bash
# Using chocolatey
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

## Local Deployment

### Development Mode

```bash
cd backend
python main.py
```

Server runs on `http://localhost:5000`

### Production Mode (Local)

```bash
cd backend
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

## Cloud Deployment

### Option 1: Heroku Deployment

1. **Install Heroku CLI:**
```bash
# Windows
choco install heroku-cli

# macOS
brew tap heroku/brew && brew install heroku
```

2. **Login to Heroku:**
```bash
heroku login
```

3. **Create Heroku App:**
```bash
heroku create your-app-name
```

4. **Add FFmpeg Buildpack:**
```bash
heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
heroku buildpacks:add heroku/python
```

5. **Set Environment Variables:**
```bash
heroku config:set ELEVENLABS_API_KEY=your_api_key_here
heroku config:set FLASK_ENV=production
```

6. **Deploy:**
```bash
git push heroku main
```

### Option 2: AWS EC2 Deployment

1. **Launch EC2 Instance:**
   - Choose Ubuntu 22.04 LTS AMI
   - t3.medium or larger (for FFmpeg processing)
   - Security group: Allow ports 80, 443, 5000

2. **Connect to Instance:**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Update System:**
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

4. **Install Dependencies:**
```bash
sudo apt-get install -y python3-pip python3-venv ffmpeg
```

5. **Clone Repository:**
```bash
git clone https://github.com/Phantom-codeer/VID_Snap_AI.git
cd VID_Snap_AI
```

6. **Setup Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

7. **Create .env File:**
```bash
cp .env.example .env
nano .env  # Add your ELEVENLABS_API_KEY
```

8. **Run with Gunicorn:**
```bash
cd backend
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

9. **Setup Nginx Reverse Proxy:**
```bash
sudo apt-get install nginx
```

Create `/etc/nginx/sites-available/vidsnap`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/vidsnap /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

10. **Setup SSL with Let's Encrypt:**
```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

### Option 3: Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/backend

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

Build and run:
```bash
docker build -t vidsnap-ai .
docker run -p 5000:5000 -e ELEVENLABS_API_KEY=your_key vidsnap-ai
```

### Option 4: DigitalOcean App Platform

1. **Connect GitHub Repository**
   - Link your VID_Snap_AI repo to DigitalOcean

2. **Create App Spec:**
   - Configure Python backend
   - Add FFmpeg buildpack
   - Set environment variables
   - Configure static file serving

## Storage Configuration

### Local Storage (Development)
- Videos stored in `frontend/static/reels/`
- Uploads in `backend/user_uploads/`

### Production Storage (AWS S3/DigitalOcean Spaces)

Add to `requirements.txt`:
```
boto3==1.26.137
```

Update path configurations:
```python
# Use AWS S3 for storing generated videos
import boto3

s3_client = boto3.client('s3')
s3_client.upload_file('video.mp4', 'bucket-name', 'videos/video.mp4')
```

## Monitoring & Logs

### Check Application Status:
```bash
sudo systemctl status vid-snapai
```

### View Logs:
```bash
# Gunicorn logs
tail -f /var/log/gunicorn/access.log

# Application logs
journalctl -u vid-snapai -f
```

## Performance Optimization

1. **Use Celery for Background Tasks:**
   - Offload video generation to task queue
   - Install: `pip install celery redis`

2. **Add Redis Cache:**
   - Cache generated videos
   - Store session data

3. **CDN for Video Delivery:**
   - Use CloudFront/Cloudflare
   - Cache `static/reels/` folder

## Database Setup (Optional)

For tracking generated videos and user data:

```bash
pip install flask-sqlalchemy
```

## Troubleshooting

**FFmpeg not found:**
```bash
# Verify installation
which ffmpeg
ffmpeg -version
```

**API Key issues:**
```bash
# Verify env variable is set
echo $ELEVENLABS_API_KEY
```

**Permission denied on upload folder:**
```bash
chmod -R 755 backend/user_uploads/
```

**Port already in use:**
```bash
# Find process using port 5000
lsof -i :5000
# Kill it
kill -9 <PID>
```

## Support

For deployment issues, check:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gunicorn Documentation](https://gunicorn.org/)
- [ElevenLabs API Docs](https://api.elevenlabs.io)
