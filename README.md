# Boggart App

Boggart is a desktop application that allows users to interact with an AI-powered chatbot. The app enhances the user experience by capturing screenshots and sending them along with user queries to provide context-aware responses.

## Features

- **AI Chatbot**: Interact with an AI-powered chatbot using OpenAI's GPT-4 model.
- **Screenshot Integration**: Automatically captures and sends screenshots with user queries for better context.
- **Responsive UI**: A clean and responsive interface built with Flet.

## Installation

### Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) (optional, for dependency management)
- [Flet](https://flet.dev/) framework

### Install Dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

Using `Poetry`:

```bash
poetry install
```

## Running the App

### As a Desktop App

Using `uv`:

```bash
uv run flet run
```

Using `Poetry`:

```bash
poetry run flet run
```

## Building the App

### Android

```bash
flet build apk -v
```

### iOS

```bash
flet build ipa -v
```

### macOS

```bash
flet build macos -v
```

### Linux

```bash
flet build linux -v
```

### Windows

```bash
flet build windows -v
```

For detailed instructions on building and signing packages, refer to the [Flet Documentation](https://flet.dev/docs/publish/).

## Project Structure

```
.
├── src/
│   ├── main.py               # Main application entry point
│   ├── screenshot_query.py   # Handles screenshot capture and query submission
│   ├── config.py             # Configuration file for API keys
│   └── assets/               # Static assets (e.g., icons)
├── storage/                  # Temporary and persistent storage
├── build/                    # Build artifacts
├── pyproject.toml            # Project metadata and dependencies
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Git ignore rules
```

## Configuration

Add your OpenAI API key in `src/config.py`:

```py
API_KEY = "your_openai_api_key"
```

## Roadmap

### Cosmetic Enhancements

- [x] Loading indicator
- [x] Text bubbles
- [ ] Background
- [x] Drop shadow
- [x] Icon
- [x] Outline on input
- [ ] Copy code button

### Functional Improvements

- [ ] Settings menu
- [ ] Chat memory
- [ ] Refresh button

### Long-Term Goals

- [ ] Ability to read and summarize websites

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the app.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flet Framework](https://flet.dev/)
- [OpenAI GPT-4](https://openai.com/)
- [Pillow Library](https://python-pillow.org/)