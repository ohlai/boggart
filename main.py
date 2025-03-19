import openai
from PIL import ImageGrab
import io
import base64
from ui import ChatInterface
import customtkinter as ctk

def take_screenshot():
    screenshot = ImageGrab.grab()
    buffered = io.BytesIO()
    screenshot.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def send_query_with_screenshot(query, screenshot):
    openai.api_key = 'your-api-key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User query: {query}\nScreenshot: {screenshot}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    root = ctk.CTk()
    chat_interface = ChatInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
