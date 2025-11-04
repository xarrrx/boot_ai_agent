import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

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

system_prompt = '''You are a helpful AI coding agent. When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.'''




available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def main():
    if len(args)==1:
        print("No prompt provided. Exiting now.")
        sys.exit(1)

    verbose = len(args) == 3 and args[2] == "--verbose"

    if verbose:
        print(f"User prompt: {user_prompt}")


    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages, 
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )

    if response.function_calls:
        for item in response.function_calls:
            print(f"Calling funtion {item.name}({item.args})")
    else:
        print(response.text)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


    '''#test print
    print (f'0: {args[0]}')
    print (f'1: {args[1]}')'''


if __name__ == "__main__":
    main()
