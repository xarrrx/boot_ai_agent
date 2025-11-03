import os
from google.genai import types


def get_files_info(working_directory, directory ="."):
    rel_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(rel_path)
    abs_working_path = os.path.abspath(working_directory)

    if not os.path.isdir(rel_path): #argument supposed to be the path nut 'just' the "directoty" ?
        #print(f'Error: "{directory}" is not a directory')
        return f'Error: "{directory}" is not a directory'

    if not abs_path.startswith(abs_working_path):
        #print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    #path checking:
    #print(f"relative path is: {rel_path}")
    #print(f"absolute path is: {abs_path}")
    #print(f"should be inside: {abs_working_path}")
    #print("----------------------------------------------------")


    result = ["Result for current directory:"]
    contents = os.listdir(abs_path)

    for item in contents:
        item_path = os.path.join(abs_path, item)
        acc = f'- {str(item)}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}'
        result.append(acc)
    

    #print("\n".join(result))
    return "\n".join(result)





schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)