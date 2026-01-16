import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ElevenLabs Configuration
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Flask Configuration
DEBUG = False
TESTING = False

# Upload Configuration
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'user_uploads')

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
