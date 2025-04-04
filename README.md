# Boggart App

Boggart is a desktop application that allows users to interact with an AI-powered chatbot. The app enhances the user experience by capturing screenshots and sending them along with user queries to provide context-aware responses.

## Features

- **AI Chatbot**: Interact with an AI-powered chatbot using OpenAI's GPT-4 model.
- **Screenshot Integration**: Automatically captures and sends screenshots with user queries for better context.
- **Responsive UI**: A clean and responsive interface built with Flet.
- **Command-Line Interface**: Use the app directly from the CLI with `screenshot_query.py`.

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

### Using the CLI with `screenshot_query.py`

You can also use the app directly from the command line by running `screenshot_query.py`. This allows you to send queries and screenshots without launching the full UI.

```bash
python src/screenshot_query.py "Your query here"
```

This will:
1. Take a screenshot of your current screen.
2. Send the screenshot and query to the AI.
3. Display the AI's response in the terminal.

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
│   ├── screenshot_query.py   # Handles screenshot capture and query submission (CLI support)
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
- [ ] Scroll to bottom button

### Functional Improvements

- [ ] Settings menu / screenshot include toggle
- [ ] Chat memory
- [ ] Refresh button
- [ ] Screenshot without the boggart window

### Long-Term Goals

- [ ] Ability to read and summarize websites
  
## Known issues
- in consistent amount of space below messages which allows user to scroll onto completely blank screen.
