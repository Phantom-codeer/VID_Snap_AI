import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import Flask app
from main import app

if __name__ == "__main__":
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', False)
    )
