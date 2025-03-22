import base64
from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def take_screenshot():
    from PIL import ImageGrab
    import io

    screenshot = ImageGrab.grab()
    buffered = io.BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def send_query_with_screenshot(query, screenshot):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{screenshot}",
                        },
                    },
                ],
            }
        ],
        stream=True,  # Enable streaming
    )
    return response

def main():
    while True:
        query = input("Enter your query: ")
        screenshot = take_screenshot()
        print("Response from LLM:")
        response = send_query_with_screenshot(query, screenshot)

        # Stream and print the response as it is generated
        try:
            for chunk in response:
                for choice in chunk.choices:
                    if choice.finish_reason != "stop":
                        print(choice.delta.content, end="", flush=True)
           
        except Exception as e:
            print(f"Error while streaming response: {e}")
        print("\n\n")  # Add a newline after the streaming is complete

if __name__ == "__main__":
    main()