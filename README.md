# ChatGPT Desktop App

This project is a desktop application for Windows that serves as a wrapper for ChatGPT (or other large language models). The application takes a screenshot of the user's desktop when they query the language model and adds that screenshot to their context input before sending it via API to the language model.

## Setup and Run

1. Clone the repository:
    ```
    git clone https://github.com/githubnext/workspace-blank.git
    cd workspace-blank
    ```

2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the application:
    ```
    python main.py
    ```

## Roadmap

- **MVP**: Build a minimum viable product with Python that captures screenshots and sends them along with user queries to the language model.
- **UI Enhancements**: Develop a full-fledged application with a nice user interface, which may or may not be in Python.
- **Cross-Platform Support**: Expand the application to support other operating systems such as macOS and Linux.
- **Additional Features**: Add more features such as saving chat history, customizing the context input, and integrating with other APIs.
