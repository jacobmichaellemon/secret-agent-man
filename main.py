import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    args = sys.argv
    content = ""
    if len(args) == 2:
        content = args[1]
    else:
        print("No arguments provided, closing agent. Try again with a CLI argument with what you want to prompt the agent!")
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = ""
    response = client.models.generate_content(
                                               model="gemini-2.0-flash-001", 
                                               contents=content)
    print(f"Agent's response: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
