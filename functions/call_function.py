
from google.genai import types
from functions import *

func_dict = {"get_files_info": get_files_info.get_files_info, "get_file_content": get_file_content.get_file_content, "run_python_file": run_python_file.run_python_file, "write_file": write_file.write_file, }

def call_function(function_call_part, verbose=False):

    function_name = function_call_part.name
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    if function_name not in func_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    args = function_call_part.args
    args["working_directory"] = "./calculator"

    
    function_result = func_dict[function_name](**args)
    


    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
    