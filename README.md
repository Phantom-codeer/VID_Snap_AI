# VID_Snap_AI

A web application that transforms images and text into engaging short-form video content with AI-generated voiceovers using the ElevenLabs API.

## Features

- **Image Upload**: Upload multiple images (PNG, JPG, JPEG)
- **AI Voice Generation**: Convert text descriptions to natural-sounding audio using ElevenLabs API
- **Video Creation**: Automatically generate videos from uploaded images with synchronized audio
- **Video Gallery**: Browse and view all generated reels
- **User-Friendly Interface**: Clean, responsive web interface built with Flask

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **API**: ElevenLabs (AI Text-to-Speech)
- **Media Processing**: FFmpeg
- **Storage**: Local file system

## Project Structure

\\\
VidsnaoAi/
 main.py                  # Flask application entry point
 config.py               # Configuration and API keys
 text_to_audio.py        # Text-to-speech conversion using ElevenLabs
 generate_process.py     # Video generation process
 templates/              # HTML templates
    base.html          # Base template
    index.html         # Home page
    create.html        # Video creation page
    gallery.html       # Video gallery page
 static/                # Static assets
    css/              # Stylesheets
    reels/            # Generated video files
    songs/            # Audio files
 user_uploads/         # User uploaded images and generated content
\\\

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg (for video processing)
- ElevenLabs API Key

### Setup

1. Clone the repository:
   \\\ash
   git clone https://github.com/Phantom-codeer/VID_Snap_AI.git
   cd VidsnaoAi
   \\\

2. Create a virtual environment:
   \\\ash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \\\

3. Install dependencies:
   \\\ash
   pip install flask elevenlabs werkzeug
   \\\

4. Install FFmpeg:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - **macOS**: \rew install ffmpeg\
   - **Linux**: \sudo apt-get install ffmpeg\

5. Configure API key:
   - Edit \config.py\ and replace \ELEVENLABS_API_KEY\ with your API key from [ElevenLabs](https://elevenlabs.io)

## Usage

1. Start the Flask server:
   \\\ash
   python main.py
   \\\

2. Open your browser and navigate to \http://localhost:5000\

3. **Create a Video**:
   - Click "Create" in the navigation
   - Upload one or more images
   - Enter a description/script
   - The application will generate a video with AI voiceover

4. **View Gallery**:
   - Click "Gallery" to view all generated videos

## How It Works

1. **Upload Phase**: User uploads images and provides text description
2. **Text-to-Speech**: Description is converted to speech using ElevenLabs API (Adam voice)
3. **Video Generation**: Images are synchronized with the generated audio using FFmpeg
4. **Storage**: Generated videos are saved to \static/reels/\ and displayed in the gallery

## API Configuration

### ElevenLabs Settings

The application uses the following voice settings:
- **Voice**: Adam (pre-made voice)
- **Model**: eleven_turbo_v2_5 (low latency)
- **Format**: MP3 at 22050 Hz
- **Stability**: 0.0
- **Similarity Boost**: 1.0
- **Speaker Boost**: Enabled

## File Upload Limits

- **Allowed formats**: PNG, JPG, JPEG
- **Storage location**: \user_uploads/{unique_id}/\

## Future Enhancements

- [ ] Multiple voice options
- [ ] Custom audio speed and tone
- [ ] Video length customization
- [ ] Download generated videos
- [ ] User authentication
- [ ] Video templates and effects
- [ ] Batch processing

## Troubleshooting

- **"Repository not found" error**: Ensure the ElevenLabs API key is valid
- **FFmpeg not found**: Install FFmpeg and add to system PATH
- **Permission denied on uploads**: Ensure \user_uploads/\ directory exists and has write permissions

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Phantom-codeer

## Support

For issues and questions, please open an issue on [GitHub](https://github.com/Phantom-codeer/VID_Snap_AI/issues).
