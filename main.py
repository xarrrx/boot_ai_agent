import os
import sys
from dotenv import load_dotenv
from google import genai 

#Load env variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
#new instance of gemini client
client = genai.Client(api_key=api_key)
#input arguments
args = sys.argv

def main():
    if len(args)==1:
        print("No prompt provided. Exiting now.")
        sys.exit(1)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=args[1]
    )
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    '''#test print
    print (f'0: {args[0]}')
    print (f'1: {args[1]}')'''


if __name__ == "__main__":
    main()
