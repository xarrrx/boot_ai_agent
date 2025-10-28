import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types

#Load env variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
#new instance of gemini client
client = genai.Client(api_key=api_key)
#input arguments
args = sys.argv

#to get the prompt after manual?
user_prompt = args[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]


def main():
    if len(args)==1:
        print("No prompt provided. Exiting now.")
        sys.exit(1)

    verbose = len(args) == 3 and args[2] == "--verbose"

    if verbose:
        print(f"User prompt: {user_prompt}")


    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages,
    )
    print(response.text)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    '''#test print
    print (f'0: {args[0]}')
    print (f'1: {args[1]}')'''


if __name__ == "__main__":
    main()
