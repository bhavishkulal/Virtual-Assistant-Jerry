

# 🤖 Jerry - Jarvis-Inspired Virtual Assistant

**A production-ready voice-controlled virtual assistant built with Python featuring advanced speech recognition, AI integration, and real-world automation capabilities.**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 🌟 Features

### 🎤 Advanced Voice Recognition
- **Smart audio processing** with dynamic energy threshold adjustment
- **Ambient noise calibration** for different environments
- **Robust error handling** with timeout and phrase limit management
- **Multi-microphone support** with device detection and selection

### 🌐 Web Automation & Integration  
- **15+ voice-activated website shortcuts** (Google, YouTube, LinkedIn, GitHub, etc.)
- **Live news fetching** from NewsAPI (focused on Indian tech, AI, and startups)
- **Music playback** with custom playlist management
- **Seamless browser integration** for instant web access

### 🧠 AI-Powered Intelligence
- **Google Gemini API integration** for natural language Q&A
- **Custom REST client** with proper error handling and timeouts
- **Intelligent command parsing** with fallback to AI for complex queries
- **Context-aware responses** for various question types

## 🛠️ Tech Stack

- **Core**: Python 3.8+
- **Speech Processing**: `speech_recognition`, `pyttsx3`
- **Web Integration**: `webbrowser`, `requests`
- **AI Integration**: Google Gemini API (custom REST client)
- **Architecture**: Modular design with clean separation of concerns

## 📁 Project Structure

jerry/
├── main.py # Main application with voice recognition loop
├── client.py # Custom Gemini API client
├── musiclibrary.py # Music playlist management
├── requirements.txt # Project dependencies
├── .gitignore # Git ignore rules
└── README.md # This file

text

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Microphone access
- Internet connection
- Google Gemini API key ([Get it here](https://aistudio.google.com/app/apikey))
- NewsAPI key ([Get free key](https://newsapi.org/))

### Installation

1. **Clone the repository**
git clone https://github.com/yourusername/jerry
cd jerry

text

2. **Create virtual environment**
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install dependencies**
pip install -r requirements.txt

text

4. **Set up environment variables**
Create a .env file or set environment variables
export GEMINI_API_KEY="your_gemini_api_key"
export NEWS_API_KEY="your_news_api_key"

text

5. **Run Jerry**
python main.py

text

## 💬 Usage Examples

### Website Navigation
- *"Open Google"* → Opens Google in default browser
- *"Open GitHub"* → Opens GitHub
- *"Open LinkedIn"* → Opens LinkedIn
- *"Open YouTube"* → Opens YouTube

### Music Control
- *"Play moh moh ke daage"* → Plays specified song from library
- *"Play vachindamma"* → Plays Telugu song

### News Updates
- *"Open news"* → Fetches latest Indian tech/AI/startup headlines

### AI Questions
- *"Ask what is machine learning?"* → Gets AI-powered answer
- *"How does Python work?"* → Intelligent response via Gemini
- *"What is the weather like?"* → Natural language query processing

### General Commands
- *"Jarvis"* → Activation acknowledgment
- *"Exit"* → Closes the application

## ⚙️ Configuration

### API Keys Setup
Jerry requires two API keys:

1. **Google Gemini API** (for AI responses)
- Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Set as environment variable: `GEMINI_API_KEY`

2. **NewsAPI** (for live news)
- Get free key from [NewsAPI.org](https://newsapi.org/)
- Set as environment variable: `NEWS_API_KEY`

### Audio Configuration
Jerry automatically detects and lists available microphones. The system calibrates for ambient noise on each startup.

## 🎯 Key Learning Outcomes

This project demonstrates:
- **Real-world API integration** (3 different APIs)
- **Audio processing** and speech recognition optimization
- **Error handling** and graceful degradation
- **Modular architecture** and clean code principles
- **Production-ready features** (logging, timeouts, calibration)

## 🔧 Advanced Features

- **Dynamic energy threshold management** prevents audio drift
- **Microphone debugging** with device listing and selection
- **Robust exception handling** for network and audio issues
- **Loop optimization** with performance monitoring
- **Modular command system** easily extensible for new features

## 🐛 Troubleshooting

### Common Issues

**Microphone not detected:**
- Check microphone permissions
- Try running with administrator privileges
- Verify microphone is not being used by other applications

**API connection errors:**
- Verify internet connection
- Check API key validity
- Ensure environment variables are set correctly

**Speech recognition issues:**
- Speak clearly and at normal pace
- Reduce background noise
- Check microphone placement and quality

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📊 Dependencies

- `SpeechRecognition>=3.8.1` - Speech recognition library
- `pyttsx3>=2.90` - Text-to-speech conversion
- `requests>=2.25.1` - HTTP requests handling
- `pyaudio>=0.2.11` - Audio I/O library

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 About This Project

Jerry is part of my journey from Python basics to AI/ML engineering. This project bridges fundamental programming concepts with real-world applications in speech recognition, API integration, and production-ready error handling.

Built during my transition into advanced Python concepts and AI/ML fundamentals as part of my public learning journey at [Bhavish Bytes](your-blog-url).

## 📬 Connect & Follow

- **Blog**: [Bhavish Bytes - Hashnode](your-hashnode-url)
- **LinkedIn**: [Your LinkedIn Profile]
- **Learning Journey**: Follow my weekly updates on advanced Python and AI/ML

---

**⭐ Star this repo if you found it helpful for your own voice assistant projects!**
