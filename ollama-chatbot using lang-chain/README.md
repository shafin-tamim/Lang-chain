# AI Chatbot with LangChain and Ollama

A modern chatbot interface built with Flask, LangChain, and Ollama using the Qwen2.5 model.

## Features

- 🎨 Modern and responsive UI with dark theme
- 💬 Real-time chat interface
- ⚡ Fast responses using Ollama
- 🔄 Typing indicators
- 🎯 Smooth animations
- 📱 Mobile-friendly design

## Prerequisites

- Python 3.8+
- Ollama installed with Qwen2.5 model
- Flask

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ollama-chatbot-using-langchain
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure Ollama is running with Qwen2.5 model:
```bash
ollama pull qwen2.5vl:3b
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
ollama-chatbot using lang-chain/
├── app.py              # Flask application
├── templates/          # HTML templates
│   └── chat.html      # Chat interface
├── requirements.txt    # Python dependencies
└── README.md          # Documentation
```

## Configuration

The chatbot uses the following configurations:

- Model: Qwen2.5 (3B parameters)
- Server: Flask development server
- Port: 5000 (default)

## Development

To modify the chat interface, edit `templates/chat.html`. The UI uses CSS variables for theming, which can be customized in the `:root` selector.

To modify the bot's behavior, adjust the prompt template in `app.py`.

## License

MIT

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request
