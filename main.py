import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()


def main():
    prompt = sys.argv[1]
    if prompt is None:
        print("No prompt provided")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )

    if response is None or response.usage_metadata is None:
        print("No response from the model")
        return

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


main()
