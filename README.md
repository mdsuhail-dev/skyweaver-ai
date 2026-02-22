# ✨ SkyWeaver.AI

**Transform your night sky observations into poetic interpretations using AI.**

---

## 📌 Overview

SkyWeaver.AI is a web application that transforms what you observe in the night sky into meaningful poetic interpretations. Describe your cosmic vision—a constellation pattern, a celestial shape, or any observation—and the app generates a poetic narrative in real-time.

**Example:**
- Input: "A dragon made of stars chasing the moon"
- Output: "A dragon made of stars speaks of untamed power and dreams that defy gravity."

---

## 🚀 Features

- **AI-Powered Interpretations** - Uses Featherless.ai language models (Llama 2 70B)
- **Real-Time Processing** - Instant results with no loading delays
- **Beautiful UI** - Responsive design with cosmic aesthetic
- **Easy to Use** - Simple input field with one-click submission
- **Mobile Compatible** - Works on all devices and screen sizes
- **Example Buttons** - Quick-start prompts for first-time users

---

## 🛠 Tech Stack

**Frontend:**
- HTML5
- CSS3 (Animations, Gradients, Backdrop Filters)
- JavaScript (Vanilla)

**Backend:**
- Python 3.9+
- Anthropic SDK (Featherless.ai integration)

**AI Model:**
- Llama 2 70B Chat via Featherless.ai
- Custom prompt engineering for poetic interpretations

---

## 📋 Project Structure

```
skyweaver-ai/
├── index.html           # Main web interface
├── skyweaver_app.py     # Python backend with API integration
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .gitignore
```

---

## 💻 Installation & Usage

### Quick Start (Web Only)
```bash
# Open the web app directly
open index.html
# or on Windows
start index.html
```

### With Python Backend
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export FEATHERLESS_API_KEY="your_api_key"

# Run backend
python skyweaver_app.py
```

---

## 📦 Dependencies

- `anthropic>=0.7.0` - Featherless.ai API client
- `python-dotenv>=1.0.0` - Environment variable management

---

## 🎨 How It Works

1. User enters their night sky observation
2. Frontend sends input to backend processing
3. AI generates poetic interpretation via Featherless.ai API
4. Result displays with animated text effect
5. User can share or generate new interpretations

---

## 🔧 API Integration

Uses Anthropic SDK to connect with Featherless.ai:

```python
from anthropic import Anthropic

client = Anthropic(api_key="your_featherless_key")
response = client.messages.create(
    model="meta-llama/llama-2-70b-chat",
    max_tokens=200,
    messages=[{"role": "user", "content": prompt}]
)
```

**Get Started:** https://featherless.ai

---

## 📱 Use Cases

- Creative writing inspiration
- Mindfulness and reflection exercises
- Educational tool for astronomy and poetry
- Personal journaling and documentation
- Social media content creation

---

## 🌐 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## 📝 License

MIT License - Free to use and modify

---

## 🔗 Repository

GitHub: https://github.com/mdsuhail-dev/skyweaver-ai
