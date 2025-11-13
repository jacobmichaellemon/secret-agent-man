import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    args = sys.argv
    args_len = len(args)
    user_prompt = ""
    verbose = ""

    if args_len == 1:
        print("No extra arguments provided, closing agent. Try again with a CLI argument with what you want to prompt the agent!")
        sys.exit(1)
    if args_len == 2:
        user_prompt = sys.argv[1]
    if args_len == 3:
        verbose = sys.argv[2]


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]), 
    ]
    response = ""
    response = client.models.generate_content(
                                               model="gemini-2.0-flash-001", 
                                               contents=messages
    )


    print(f"Agent's response: {response.text}")
    if verbose == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
