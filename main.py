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
    completion = client.chat.completions.create(
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
    )
    return completion.choices[0].message.content

def main():
    query = input("Enter your query: ")
    screenshot = take_screenshot()
    response = send_query_with_screenshot(query, screenshot)
    print("Response from LLM:", response)

if __name__ == "__main__":
    main()


